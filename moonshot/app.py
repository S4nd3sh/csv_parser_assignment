import os
import re
import sys
import csv
import string
import argparse
import stopwords
import logging
import emoji
from io import StringIO
from moonshot.db import insert_to_collections
from moonshot.constants import DB_NAME, COLLECTION_NAME
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

FILE_PATH = os.path.join(os.path.dirname(__file__), "initial_dir/raw.csv")
POST_PROCESS_DIR = os.path.join(os.path.dirname(__file__), "post_processing")


def cli_args():
    """
    To parse arguments supplied to parse Moonshot CSV file
    """
    parser = argparse.ArgumentParser("Moonshot CSV parser")

    parser.add_argument(
        "--path",
        "-p",
        required=False,
        help="path to your csv file" "-p //path/to/your/file.csv",
        type=str,
        default=FILE_PATH,
    )

    parser.add_argument(
        "--stop-words",
        "-s",
        required=False,
        nargs="+",
        help="you can supply additional stop words other than the default if required"
        "-s additional stop words",
    )
    argv = sys.argv[1:]
    args = parser.parse_args(argv)
    if not os.path.exists(args.path):
        raise FileNotFoundError(f"File '{args.path}' doesn't exist")
    return args


def remove_emoji(text):
    # https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
    return emoji.replace_emoji(text, replace="")


def remove_punctuations(text):
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    return text.translate(str.maketrans("", "", string.punctuation))


def process_text(text, additional_stop_words=""):
    # Remove standard stop words of English from the text
    text = stopwords.clean(text.lower().split(), "en")

    if additional_stop_words:
        text = " ".join([word for word in text if word not in additional_stop_words])

    # remove emoji
    text = remove_emoji(" ".join(text))

    # remove numbers
    text = re.sub("[\-\+]{,1}[0-9]+(\.[0-9]+)*\s*[KMBkmb]*", " ", text)

    # remove punctuations
    text = remove_punctuations(text)

    # remove multiple spaces and return
    return re.sub("\\s+", " ", text).strip()


def read_csv(path):
    file = open(path, "r")
    text = file.read()
    text = re.sub(',\\s"', ',"', text)
    csv_data = StringIO(text)
    csv_reader = csv.DictReader(csv_data, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")

    rows = []
    for row in csv_reader:
        rows.append(row)
    return rows


def word_frequency(text):
    freq = dict()
    for word in text.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def move_file_2_post_processing(source_file_path):
    # Move file from initial_dir to post_processing directory
    base_name = os.path.basename(source_file_path)
    dest_file_path = os.path.join(POST_PROCESS_DIR, base_name)
    logging.info(f"Moving: {source_file_path} >> {dest_file_path}")
    os.rename(source_file_path, dest_file_path)


def save_data_2_database(csv_data):
    logging.info("Saving parsed csv data along with it's word frequencies to MongoDB")
    logging.info(f"Database name: {DB_NAME}")
    logging.info(f"Collection name: {COLLECTION_NAME}")    
    insert_to_collections(
        database_name=DB_NAME, collection_name=COLLECTION_NAME, data=csv_data
    )
    logging.info("Data save successful.")


def post_process(source_file_path, csv_data):
    logging.info("-- Commencing post-processing operations --")
    # Move file to another location
    move_file_2_post_processing(source_file_path=source_file_path)

    # save data to database
    save_data_2_database(csv_data)    

def main():
    args = cli_args()
    logging.info("Parsing csv ...")
    csv_data = read_csv(args.path)
    logging.info("Parsing complete. ")

    logging.info("Cleaning text field and calculating word frequencies...")
    for row in csv_data:
        text = process_text(
            text=row["original_text"], additional_stop_words=args.stop_words
        )
        row["word_frequencies"] = word_frequency(text)
        row["_id"] = row.pop("id")

    logging.info("CSV parsing and text cleaning successful. ")
    post_process(source_file_path=args.path, csv_data=csv_data)
    logging.info("..\n\t-- Moonshot csv-parser completed successfully. --")


if __name__ == "__main__":
    main()
