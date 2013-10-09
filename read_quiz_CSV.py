import csv

# Open CSV file
quiz_filename = '/path/to/file/[00000086] CSV Quiz Responses [23].csv'
quizfile = open(quiz_filename, 'r')

# Read CSV file to list quiz
quizreader = csv.reader(quizfile)
quiz = []
for row in quizreader:
    quiz.append(row)

# Sum the number of responses for each option
option = []
rowID = 3
colID = 3
for i in range(int(len(quiz[0]))-3):
    option_total = 0
    rowID = 3
    for j in range(len(quiz)-3):
        option_total += int(quiz[rowID][colID])
        rowID += 1
    option.append(option_total)
    colID += 1
