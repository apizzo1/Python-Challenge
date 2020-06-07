import csv
import os

#create and initialize variables needed
rowcount = 0
votetally = []
candidates = []
wincount= 0

#navigate to data file
election_data = os.path.join("Resources", "election_data.txt")

#read data file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    csv_header = next(csvreader)

    for row in csvreader:
        #count the number of voters
        rowcount = rowcount + 1
        #make a list of the vote results
        votetally.append(row[2])

#create set of unique candidates       
candidates = set(votetally)      

#Print results

#Print results to a txt file

f= open("Analysis/Results_PyPoll.txt","w")

f.write(f"""

Election Results
------------------------
Total Votes: {rowcount}
------------------------
""")

#Print results in terminal
print(f"""

Election Results
------------------------
Total Votes: {rowcount}
------------------------""")

#Calculate vote percentages
for cand in candidates:
    percentage = (votetally.count(cand)/rowcount)*100
    #update percentage format to 3 decimals
    percent_format = "{:.3f}".format(percentage)
    #Print each candidate, their vote percentage and the number of votes they received
    print(f'{cand}: {percent_format}% ({votetally.count(cand)})')
    f.write(f"{cand}: {percent_format}% ({votetally.count(cand)})\n")
    #Find winner
    if percentage > wincount:
        winner = cand
        wincount = percentage
print(f"""------------------------
Winner: {winner}
------------------------
""")

f.write(f"""------------------------
Winner: {winner}
------------------------

""")
#close txt file
f.close() 