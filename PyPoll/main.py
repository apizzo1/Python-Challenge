import csv
import os

rowcount = 0
votetally = []
candidates = []

election_data = os.path.join("Resources", "election_data.txt")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    
    #count the number of voters
    for row in csvreader:
        rowcount = rowcount + 1
        votetally.append(row[2])
        

candidates = set(votetally)

print(f"""

Election Results
------------------------
Total Votes: {rowcount}
------------------------

""")