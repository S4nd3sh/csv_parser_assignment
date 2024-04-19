# MoonShot - Software Developer – Technical Assessment

## CSV Parser - Assignment information
This library is used to perform cleaning of text present in CSV.  
The below is the details of assignment provided.  

### Write a Word Frequency program that:  
<ul>
  <li>
     Reads a CSV (comma-separated values) file from a folder (see description and sample on page 2)
  </li>  
  <li>
    Performs a word frequency count on the text in the “original_text” segment (the third segment)
  </li> 
  <ol>
        <li> The count should ignore a predefined set of common words (e.g. “a”,  “the”, “then”, “and”, “an”, etc)  </li>
        <li> It should ignore numbers in numeric form within the text (e.g. “100”, “1.250”) but numbers spelled out as words (e.g. “three”, “thousand”) is allowed and should be counted  </li>
        <li> It should ignore emojis </li> 
    </ol>
    <li>The results should be stored in a database along with the original fields in the CSV file
    </li> 
    <li>
    The original file should be moved to another folder once processing is complete  
    </li>  
</ul>  

### Requirements and Constraints
<ul>
    <li>Use Python</li>
    <li>Your code should work and run - please provide instructions!</li>
    <li>There is no need for authN or authZ</li>
    <li>There is no need for deployment or infrastructure management, your solution just needs to run locally for us when we receive it</li>
    <li>Please make your solution available publicly on a source code management system or supply as a zipped file</li>
</ul>

## Setting up environment 
- Install Poetry using pip command `pip install poetry` for your default python   
- Initialise and activate your virtual environment: Change into '\moonshot' directory in your terminal where pyproject.toml file exists and execute  `poetry shell`  
- Activate your environment on new terminal: `poetry shell`  
- Install package: `poetry install` within your virtual environment  
- Deactivate your environment: `deactivate`  
- List your poetry environments: `poetry env list`  
- Delete your poetry environment: `poetry env remove name_of_env`

## Setting up database

Initialise MongoDB NoSql database to save original text and word frequencies using the command below. 

Note: Initialisation of the database requires Docker pre-installed on your machine. 

RUN: `> init-database`  

```
Document 1: {"_id": 1234, "source": "Online", "original_text": "this is a sentence with the word sentence repeated again", "word_frequencies": {"sentence": 2, "word": 1, "repeated": 1}}

Document 2: {"_id": 1235, "source": "Online", "original_text": "test sentence similar to sentence in document 1", "word_frequencies": {"test": 1, "sentence": 2, "similar": 1, "document": 1}}
```

## App usage
To run CSV parsing after installation of the package. 
`csv-parser --path '\\path\to\your\raw.csv' --stop-words additional stop words`  

- <code>--path</code>:  
  If <code>--path</code> argument is not supplied it defaults to '..\moonshot\initial_dir\raw.csv' present within the library. 
- <code>--stop-words</code>:  
  This argument appends more stop words to existing list of stop-words.
  Stop words for this library are retrieved through the stopwords library -
  https://github.com/astuanax/stopwords/tree/master 
- <code>--ignore-database</code>:  
  If <code>--ignore-database</code> this flag is set database insert will be skipped. 

### Running tests
Run `pytest` while staying in the directory that contains 'tests' dir. 