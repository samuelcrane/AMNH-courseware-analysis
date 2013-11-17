# Samuel Crane
# https://github.com/samuelcrane
#
# This Python script takes the CSV Survey Response file from Coursera
# and makes a new file that contains the Coursera universal user ID 
# for each member of the groups that you define. The idea here is to 
# split learners into groups based on their survey responses for 
# analysis of performance and activity across the groups. This userID
# table can then be used when extracting data from the SQL dump. 
#
# Input file loosely of format:
# +---------+----------+---------+
# | user_ID | educator | student |
# +---------+----------+---------+
# |  55555  |    1     |    0    |
# |  66666  |    0     |    1    |
# +---------+----------+---------+
#
# Output file loosely of format:
# +----------+---------+
# | educator | student |
# +----------+---------+
# |  55555   |  66666  |
# +----------+---------+

import csv

# Open the Coursera-provided CSV file.
surveyfile_path = '/Users/sc/Dropbox/data/Genetics/surveys/precourse/build/input/'
surveyfile_name = '[00000099] CSV Quiz Responses [53].csv'
surveyfile = open(surveyfile_path + surveyfile_name, 'r')

# Specify output path and output file names
outputfile_path = '/Users/sc/Dropbox/data/Genetics/surveys/precourse/build/output/'
educatorgroupfile_name = 'educatorgroup.csv'
 
surveyreader = csv.reader(surveyfile)
survey = []
for row in surveyreader:
    survey.append(row)

# Initialize groups
educator = []
student = []
retired = []
other = []
not_educator = []

# Populate groups with user_IDs
rowID = 3
colID = 3
for i in range(1, 5):
    rowID = 3
    if survey[2][colID] == 'educator':
        for j in range(len(survey) - 3):
            if survey[rowID][colID] == '1':
                educator.append(survey[rowID][0])
            rowID += 1
    elif survey[2][colID] == 'student':
        for j in range(len(survey) - 3):
            if survey[rowID][colID] == '1':
                student.append(survey[rowID][0])
            rowID += 1
    elif survey[2][colID] == 'retired':
        for j in range(len(survey) - 3):
            if survey[rowID][colID] == '1':
                retired.append(survey[rowID][0])
            rowID += 1
    elif survey[2][colID] == 'other':
        for j in range(len(survey) - 3):
            if survey[rowID][colID] == '1':
                other.append(survey[rowID][0])
            rowID += 1
    colID += 1

# Make one long list of all the learners who simply aren't an educator
for row in student:
    not_educator.append(row)
for row in retired:
    not_educator.append(row)
for row in other:
    not_educator.append(row)

# Add question column headers
educator.insert(0,'educator')
student.insert(0,'student')
retired.insert(0,'retired')
other.insert(0,'other')
not_educator.insert(0,'not_educator')

# Export
groups = [educator,student,retired,other,not_educator]
rows = map(None, *groups)
with open(outputfile_path + educatorgroupfile_name, 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(rows)





