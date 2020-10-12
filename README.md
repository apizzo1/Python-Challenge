# Python-Challenge

This challenge was to perform basic analyses using Python in real-world scenarios.

## Challenge Details 

### PyBank Challenge

This challenge was to utilize the budget_data.csv to perform the following analyses:
* Find the total number of months included in the dataset
* Calculate net total amount of "Profit/Losses" over the entire period
* Calculate average of the changes in "Profit/Losses" over the entire period
* Find greatest increase in profits (date and amount) over the entire period
* Find greatest decrease in losses (date and amount) over the entire period

This script prints the results to the terminal and a text file, stored in the Analysis folder.

### PyPoll Challenge

Using the election_data.csv, the following analyses were performed:
* Find total number of votes cast
* Find a complete list of candidates who received votes 
* Calculate the percentage of votes each candidate won
* Find total number of votes each candidate won
* Determine the winner of the election based on popular vote.

This script prints the results to the terminal and a text file, stored in the Analysis folder.

### PyBoss Challenge

Using employee_data.csv, the following actions were performed:

* Convert the dataset format in the following ways:
    * Name column to First Name, Last Name (2 fields instead of one)
    * Convert birthdate format from YYYY-MM-DD to MM/DD/YYYY
    * Convert social security numbers from ###-##-#### to ***-**-####
    * Convert State field from full state name to state abbreviation (using [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5))
    
This script exports a results csv file with the above changes included.

### PyParagraph

This challenge requires importing text file samples and analyzing them for the following:
* Approximate word count
* Approximate sentence count
* Approximate letter count (per word)
* Average sentence length (in words)

Main.py runs analysis on paragraph_1.txt (found in Resources folder). Main2.py runs analysis on paragraph_2.txt (found in Resources folder).

Both scripts print the results to the terminal and a text file, stored in the Analysis folder.

Note:
The scripts consider words with hyphens as one word - therefore, the code yields the same as what Microsoft Word word count would yield.This is important for paragraph_2 analysis, for words such as "career-defining" being identified as one word in the word count.
    
## Files Included

Each folder contains files with the same names:
* Resources folder - contains the data file(s) to be analyzed
* Analysis folder - contains .txt output of analysis results
* main.py file - contains code to perform analyses
