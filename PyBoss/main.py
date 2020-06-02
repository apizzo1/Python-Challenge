import csv
import os
import datetime

first = []
last = []
names = []
newdate = []
SSN_change = []



employee_data = os.path.join("Resources", "test3.csv")

with open(employee_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        a, b = row[1].split(' ')
        first.append(a)
        last.append(b)
        #convert date
        #srouce: https://stackoverflow.com/questions/14524322/how-to-convert-a-date-string-to-different-format
        newdate.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y'))
        #source: https://stackoverflow.com/questions/22586286/python-is-there-an-equivalent-of-mid-right-and-left-from-basic
        new_ssn = "***-**-" + str(row[3][7:])
        SSN_change.append(new_ssn)
print(SSN_change)
