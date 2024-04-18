import os
import re
import sys
import csv
import string
import argparse
import stopwords
import emoji
from io import StringIO

FILE_PATH = os.path.join(os.path.dirname(__file__), "initial_dir/raw.csv")


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


def clean_text(text, additional_stop_words=""):
    # Remove standard stop words of English from the text
    text = stopwords.clean(text.lower().split(), "en")

    if additional_stop_words:
        text = " ".join(
            [word for word in text if word not in additional_stop_words]
        )
    
    # remove emoji 
    text = remove_emoji("".join(text))
    
    # remove numbers 
    text = re.sub("[\-\+]{,1}[0-9]+(\.[0-9]+)*\s*[KMBkmb]*", " ", text) 
    
    # remove punctuations
    text = remove_punctuations(text)

    # remove multiple spaces and return
    return re.sub("\\s+", " ", text).strip()


def read_csv(path):
    file = open(path, "r")
    text = file.read()       
    text = re.sub(',\\s\"', ',\"', text)
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

def main():
    args = cli_args()
    csv_data = read_csv(args.path)
    word_frequencies = []
    for row in csv_data:
        text = clean_text(text=row['original_text'],additional_stop_words= args.stop_words)
        word_frequencies.append(word_frequency(text))
    breakpoint()
    return word_frequencies


if __name__ == "__main__":
    main()
