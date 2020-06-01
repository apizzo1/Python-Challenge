import csv
import os

rowcount = 0
Net_change = 0
profit_counter = []
change = []
dates = []

budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    
    #count the number of months
    for row in csvreader:
        rowcount = rowcount + 1
        profit_counter.append(int(row[1]))
        dates.append(row[0])
        
Net_change = sum(profit_counter)    

#Reverse list of profits/losses
profit_counter.reverse()

for i in range((len(profit_counter)) -1):
    change.append(profit_counter[i] - profit_counter[i+1])

average = round(sum(change)/len(change),2)

max_inc = max(change)
max_dec = min(change)
inc_date = dates[len(dates) - (change.index(max_inc) +1)]
dec_date = dates[len(dates) - (change.index(max_dec) +1)]

#Summary of Analysis
print(f"""
Financial Analysis       
-------------------------     
Total Months: {rowcount} 
Total: ${Net_change}
Average Change: ${average}
Greatest Increase in Profits: {inc_date} (${max_inc})
Greatest Decrease in Profits: {dec_date} (${max_dec})
""")