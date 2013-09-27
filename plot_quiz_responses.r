# Samuel Crane
# http://www.samuelcrane.com
# https://github.com/samuelcrane
#
# R code
# Updated: 2013-09-27
# Faceted bar chart of quantitative quiz results from Coursera MOOC data
# Format of CSV input file:
# question,option,responses,option_text
# 1,1,2227,option text
# 1,2,112,option text
# ...


library('ggplot2')

# Faceted bar charts of Quiz Question responses
# The input CSV file here is a cleaned version of the Quiz Summary TXT file that Coursera provides
quizResp <- read.csv('/Week3/plot/input/quiz_response_table.csv')
quizNumber <- "Quiz 3 Question Responses"
qh <- ggplot(quizResp, aes(x=option, y=responses)) 
qh <- qh + geom_bar(binwidth=.5, colour="black", fill="white", stat="identity")
qh <- qh + facet_grid(. ~ question)
qh <- qh + labs(title = quizNumber, x = "Question Option", y = "Number of Responses") 
qh
