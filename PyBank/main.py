import csv
import os

#initialize variables
rowcount = 0
profit_counter = 0
max_inc = 0
max_dec = 0
sum_change = 0

#import data file
budget_path = os.path.join("Resources", "budget_data.csv")

#Open and read data file
with open(budget_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    csv_header = next(csvreader)

    #count the number of months
    for row in csvreader:
        rowcount = rowcount + 1
        #sum the net_change
        profit_counter = profit_counter + int(row[1])
        #must start at row 2 because we cannot subtract previous profit from row 1, since there is no previous profit before row 1
        if rowcount >= 2:
            #get the profit change between current and previous rows
            current = int(row[1]) - prev_profit
            #sum the changes to calculate average change later
            sum_change = sum_change +current
            #find the greatest profit increase and decrease
            if current > max_inc:
                max_inc = current
                inc_date = row[0]
            if current < max_dec:
                max_dec = current
                dec_date = row[0]
        #set previous profit for next iteration
        prev_profit = int(row[1])

#calculate average change 
avg_change = round(sum_change/(rowcount-1),2) 

#Summary of Analysis
#create txt file to print to
f= open("Analysis/Results_PyBank.txt","w")

#write results to txt file
f.write(f"""
Financial Analysis       
-------------------------     
Total Months: {rowcount} 
Total: ${profit_counter}
Average Change: ${avg_change}
Greatest Increase in Profits: {inc_date} (${max_inc})
Greatest Decrease in Profits: {dec_date} (${max_dec})
""")
#close txt file
f.close() 

#print results to terminal
print(f"""
Financial Analysis       
-------------------------     
Total Months: {rowcount} 
Total: ${profit_counter}
Average Change: ${avg_change}
Greatest Increase in Profits: {inc_date} (${max_inc})
Greatest Decrease in Profits: {dec_date} (${max_dec})
""")