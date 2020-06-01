import csv
import os

rowcount = 0

budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    
    #count the number of months
    for row in csvreader:
        rowcount = rowcount + 1



#Summary of Analysis
print(f"""
Financial Analysis       
-------------------------     
Total Months: {rowcount} 
""")