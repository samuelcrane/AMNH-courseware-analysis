# Samuel Crane
# https://github.com/samuelcrane
#
# This Python script takes the CSV Survey Response file from Coursera
# and makes a new file that contains the Coursera universal user ID 
# for each member of the groups that you define. The idea here is to 
# split learners into groups (in SQL) based on their survey responses for 
# analysis of performance and activity across the groups. This userID
# table can then be used when extracting data from the SQL dump. 
#
# This script handles radio-style buttons (where only one option is 
# permitted) and checkbox-style questions (where multiple choices are 
# allowed for a single user_id). The output is a CSV file that can be 
# imported directly into Sequel Pro, where the field names are indexed
# question numbers, ready to be joined with any user data in the database.
# A table mapping the question index numbers to the qctual question text
# is also generated. 
#
# Input file loosely of format:
# +---------+----------+---------+-----------+-----------+
# | user_ID | educator | student | 1-2 hours | 3-4 hours |
# +---------+----------+---------+-----------+-----------+
# |  55555  |    1     |    0    |     0     |     1     |
# |  66666  |    0     |    1    |     1     |     0     |
# +---------+----------+---------+-----------+-----------+
#
# responses.csv loosely of format:
# +-----------+------------+------------+
# |  user_id  | Question 1 | Question 2 |
# +-----------+------------+------------+
# |   55555   |  educator  |  3-4 hours |
# +-----------+------------+------------+
# |   66666   |  student   |  1-2 hours |
# +-----------+------------+------------+
#
# question_indices.csv loosely of format:
# +-------------+---------------------------+
# | Question ID | Question Text             | 
# +-------------+---------------------------+
# | Question 1  |  What's your role?        |
# +-------------+---------------------------+
# | Question 2  |  How many hours per week? |
# +-------------+---------------------------+
#

import csv

# Open the Coursera-provided CSV file.
surveyfile_path = '/Earth/surveys/precourse/build/input/'
surveyfile_name = '[00000043] CSV Quiz Responses [17].csv'
surveyfile = open(surveyfile_path + surveyfile_name, 'r')

# Specify output path and output file names
outputfile_path = '/Earth/surveys/precourse/build/output/'
replace_name = 'precourse_responses.csv'

# Identify the columns that correspond to checkbox-style questions
# where multiple choices are allowed. 
checkbox = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326]

print 'Reading survey file...'
surveyreader = csv.reader(surveyfile)
survey = []
for row in surveyreader:
    survey.append(row)

surveyfile.close()

print 'Parsing survey responses...'
rowID = 3
colID = 5
responses = []
headers = []
headers.append('user_id')
questionID = survey[1][colID]

while rowID < len(survey):
    colID = 5
    user_row = []
    user_row.append(survey[rowID][1])
    prior_length = len(user_row)
    questionID = survey[1][colID]
    while colID < len(survey[0]):
        # Before doing checkbox questions, check if previous question
        # was not answered. Fill in with NA if not. 
        if colID in checkbox and len(user_row) == prior_length:
            user_row.append('NA')
            if rowID == 3:
                headers.append(survey[1][colID - 1])
        # If previous question was answered, do checkbox questions
        elif colID in checkbox and len(user_row) > prior_length:
            # All Affirmatives get filled with response text
            if survey[rowID][colID] == '1':
                user_row.append(survey[2][colID])
                if rowID == 3:
                    headers.append(survey[1][colID])
                colID += 1
            # All negatives get NA
            else:
                user_row.append('NA')
                if rowID == 3:
                    headers.append(survey[1][colID])
                colID += 1
        # Check question status, proceed if same question
        elif survey[1][colID] == questionID:
            # Affirmatives get filled with response text
            if survey[rowID][colID] == '1':
                user_row.append(survey[2][colID])
                if rowID == 3:
                    headers.append(survey[1][colID])
                colID += 1
            # Negatives get skipped
            else:
                colID += 1
        # At the end of a question block, see if any response was provided
        # If not, fill in with NA
        elif len(user_row) == prior_length:
            user_row.append('NA')
            if rowID == 3:
                headers.append(survey[1][colID - 1])
            prior_length = len(user_row)
            questionID = survey[1][colID]
        # If response was provided, carry on with new question
        else:
            questionID = survey[1][colID]
            prior_length = len(user_row)
    responses.append(user_row)
    rowID += 1

# Massage the headers for MySQL
print 'Building column headers...'
headers_index = []
question_number = 0
option_number = 1
for index, value in enumerate(headers):
    if headers[index] == headers[index - 1]:
        option_number += 1
        headers_index.append('Q'+str(question_number - 1)+'.'+str(option_number))
    else:
        option_number = 1
        headers_index.append('Q'+str(question_number)+'.'+str(option_number))
        question_number += 1
headers_index[0] = 'user_id'
    
responses.insert(0, headers_index)
print 'Writing output file...'
output_file = open(outputfile_path+replace_name, 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(responses)
output_file.close()

headers_index[0] = 'Question Index'
headers[0] = 'Question Text'
question_indices = [headers_index,headers]
rows = map(None, *question_indices)
with open(outputfile_path + 'precourse_question_indices.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(rows)
print 'Done.'
