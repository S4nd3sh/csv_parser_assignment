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
Install Poetry using pip command `pip install poetry`

Initialise and activate your virtual environment: Change into '\moonshot' directory in your terminal where pyproject.toml file exists and execute  `poetry shell`  
Activate your environment on new terminal: `poetry shell`  
Install package: `poetry install` within your virtual environment  
Deactivate your environment: `deactivate`  
List your poetry environments: `poetry env list`  
Delete your poetry environment: `poetry env remove name_of_env`

## Usage 
To run CSV parsing after installation of the package. 
`csv-parser --path '\\path\to\your\raw.csv' --stop-words additional stop words` 

If not supplied it defaults to file.csv in the library

