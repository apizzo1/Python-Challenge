import csv
import os
import datetime

#create and initialize variables needed
emp_id = []
first = []
last = []
names = []
newdate = []
SSN_change = []
state = []
New_Data = []

#create dictionary of states and their abbreviations
#Source: https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#navigate to data file
employee_data = os.path.join("Resources", "employee_data.csv")

#read the data file
with open(employee_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #skip header
    csv_header = next(csvreader)

    for row in csvreader:
        #create a list of emp IDs
        emp_id.append(row[0])
        #split the Name column into first name and last name
        #add first names to a list and last names to a different list
        a, b = row[1].split(' ')
        first.append(a)
        last.append(b)
        #convert date and add to a list
        #source: https://stackoverflow.com/questions/14524322/how-to-convert-a-date-string-to-different-format
        newdate.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y'))
        #slice the SSN data to only show last 4 characters and concantenate with ***-**-
        #source: https://stackoverflow.com/questions/22586286/python-is-there-an-equivalent-of-mid-right-and-left-from-basic
        new_ssn = "***-**-" + str(row[3][7:])
        #add new SSNs to a list
        SSN_change.append(new_ssn)
        #convert state to just state abbreviation and add to a list
        state.append(us_state_abbrev[str(row[4])])

#zip all the lists together and create a new list of data
New_Data = list(zip(emp_id,first,last,newdate,SSN_change,state))

#specify output file location
output_data = os.path.join("Analysis", "Results.csv")

#create and write data to output file
with open(output_data, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",")
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    for row in New_Data:
        csvwriter.writerow(row)
