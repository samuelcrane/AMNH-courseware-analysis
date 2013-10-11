# Create a table of survey response rates for each question from the 
# Coursera export source file CSV Quiz Responses (of survey repsonses).
# This sums the responses for each option, strips out the one text
# response we have in our survey, and makes two files: one of the 
# question responses and one containing just the text responses. 
# 
# Samuel Crane
# https://github.com/samuelcrane

import csv

# Open the Coursera-provided CSV file.
surveyfile_path = '/Users/sc/Dropbox/data/Earth/Week1/build/input/'
surveyfile_name = '[00000004] CSV Quiz Responses [17].csv'
surveyfile = open(surveyfile_path + surveyfile_name, 'r')

# Read said CSV file to a list called quiz. 
surveyreader = csv.reader(surveyfile)
survey = []
for row in surveyreader:
    survey.append(row)

# Remove the zipcode question into its own list called zipcode
# This is the only text response in the quiz and is treated differently
zipcode = []
rowID = 0
colID = 266
for i in range(len(survey)):
    zipcode.append(survey[rowID].pop(colID).rstrip())
    rowID += 1
zipcode = filter(None, zipcode)

# Sum the number of responses for each question option and 
# place the sums into a list called option_responses. 
option_responses = []
rowID = 3
colID = 3
for i in range(int(len(survey[0])) - 3):
    option_total = 0
    rowID = 3
    for j in range(len(survey) - 3):
        option_total += int(survey[rowID][colID])
        rowID += 1
    option_responses.append(option_total)
    colID += 1

# Place the text of each question option into a list called option_text.
option_text = survey[2][3:]
question_text = survey[1][3:]

# Add column headers to each list as the first item in the list.
option_responses.insert(0,'responses')
option_text.insert(0,'option_text')
question_text.insert(0,'question_text')

# Write the selected lists as columns to a CSV formatted output file.  
rows = zip(option_responses,option_text,question_text)
with open('/Users/sc/Dropbox/data/Earth/Week1/build/output/survey_response_table.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(rows)

# Write the zipcodes to a txt file
rows = zip(zipcode)
with open('/Users/sc/Dropbox/data/Earth/Week1/build/output/survey_zipcodes.txt', 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(rows)
