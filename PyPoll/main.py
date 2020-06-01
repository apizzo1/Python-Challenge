import csv
import os

rowcount = 0
votetally = []
candidates = []
wincount= 0

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
------------------------""")
for cand in candidates:
    percentage = round((votetally.count(cand)/rowcount)*100,3)
    print(f'{cand}: {percentage}% ({votetally.count(cand)})')
    if percentage > wincount:
        winner = cand
        wincount = percentage
print(f"""------------------------
Winner: {winner}
------------------------
""")
