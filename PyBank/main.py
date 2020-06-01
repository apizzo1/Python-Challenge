import csv
import os

rowcount = 0
profit_counter = []
Net_change = 0 
change = []

budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    
    #count the number of months
    for row in csvreader:
        rowcount = rowcount + 1
        profit_counter.append(int(row[1]))
        
Net_change = sum(profit_counter)    

#Reverse list of profits/losses
profit_counter.reverse()

for i in range((len(profit_counter)) -1):
    change.append(profit_counter[i] - profit_counter[i+1])

average = round(sum(change)/len(change),2)

#Summary of Analysis
print(f"""
Financial Analysis       
-------------------------     
Total Months: {rowcount} 
Total: ${Net_change}
Average Change: ${average}
""")