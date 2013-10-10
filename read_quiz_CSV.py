# Create a table of quiz question responses from the Coursera export 
# source file CSV Quiz Responses. This file is similar in format to 
# the deprecated Quiz Summary source file.  
# 
# Samuel Crane
# https://github.com/samuelcrane

import csv

# Open the Coursera-provided CSV file.
quizfile_path = '/Users/sc/Dropbox/data/Genetics/Week4/build/input/'
quizfile_name = '[00000086] CSV Quiz Responses [23].csv'
quizfile = open(quizfile_path + quizfile_name, 'r')

# Read said CSV file to a list called quiz. 
quizreader = csv.reader(quizfile)
quiz = []
for row in quizreader:
    quiz.append(row)

# Sum the number of responses for each question option and 
# place the sums into a list called option_responses. 
option_responses = []
rowID = 3
colID = 3
for i in range(int(len(quiz[0]))-3):
    option_total = 0
    rowID = 3
    for j in range(len(quiz) - 3):
        option_total += int(quiz[rowID][colID])
        rowID += 1
    option_responses.append(option_total)
    colID += 1

# Place the text of each question option into a list called option_text.
option_text = quiz[2][3:]

# Make a list of question numbers (1-10) for the column called question.
# There are always exactly 10 questions in our quizzes.  
question = []
number_of_questions = 10
number_of_options = 4
index = 1
for i in range(number_of_questions):   
    for j in range(number_of_options):
        question.append(str(index))
    index += 1

# Make a list of option numbers (1-4) for the column called question.
# Each question always has exactly 4 options in our quizzes. 
option = []
number_of_questions = 10
number_of_options = 4
question_index = 1
option_index = 1
for i in range(number_of_questions):
    option_index = 1
    for j in range(number_of_options):
        option.append(str(option_index))
        option_index += 1
    question_index += 1

# Add column headers to each list as the first item in the list.
question.insert(0,'question')
option.insert(0,'option')
option_responses.insert(0,'responses')
option_text.insert(0,'option_text')

# Write the selected lists as columns to a CSV formatted output file.
# See the example output file 'quiz_response_table.csv'.   
rows = zip(question,option,option_responses,option_text)
with open('/Users/sc/Dropbox/data/Genetics/Week4/build/output/quiz_response_table.csv', 'wb') as fin:
    writer = csv.writer(fin, delimiter = ',')
    writer.writerows(rows)
