# Python-Challenge

Notes on PyBoss:
1. Output file matches answer seen in HW description.

Notes on PyParagraph:
1. Main.py runs analysis on paragraph_1.txt. Main2.py runs analysis on paragraph_2.txt - both analyses have their own output files

2. For the example given in the instructions, I am considering words with hyphens as one word - therefore, my code yields 120 words (same as if Microsoft Word were to count the words in this text snippet.This is important for paragraph_2 analysis, for words such as "career-defining" being identified as one word in word count.

3. For Paragraph 2, comparing to the results Erwins posted in Slack, my code returns slightly different numbers. I only see 10 sentences, and that is what my code returns. I also have a slightly different word count, which is the same as what Microsoft Word shows.

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

From employee_data.csv, the following actions and analyses were performed:

* Convert the dataset format in the following ways:
    * Name column to First Name, Last Name (2 fields instead of one)
    * Convert birthdate format from YYYY-MM-DD to MM/DD/YYYY
    * Convert social security numbers from ###-##-#### to ***-**-####
    * Convert State field from full state name to state abbreviation (using [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5))
    
## Files Included

Each folder contains files with the same names:
* Resources folder - contains the data file to be analyzed
* Analysis folder - contains .txt output of analysis results
* main.py file - contains code to perform analysis
