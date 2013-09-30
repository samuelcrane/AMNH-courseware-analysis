# Samuel Crane
# http://www.samuelcrane.com
# https://github.com/samuelcrane
#
# R code
# Updated: 2013-09-30
# Time Series plots for weekly or daily activity data from Coursera MOOC data
# Transpose the CSV file before reading it. 

library('ggplot2')

# Read in and parse daily activity
# Before this step, I've transposed the CSV file that Coursera provides under the Data -> Download Statistics
daily <- read.csv("daily.csv")
# Subset the data by a week or a few days
daily_slice <- daily[135:155,]
daily_slice <- cbind(daily_slice, session = "amnhgenetics001")

# Read in weekly data
weekly <- read.csv("weekly_summary.csv")
weekly_slice <- weekly[157:159,]
weekly_slice <- cbind(weekly_slice, session = "amnhgenetics001")


# Faceted bar charts of Quiz Question responses
# The input CSV file here is a cleaned version of the Quiz Summary TXT file that Coursera provides
# See example quiz_response_table.csv file
quizResp <- read.csv('quiz_response_table.csv')
quizNumber <- "Quiz 3 Question Responses"
qh <- ggplot(quizResp, aes(x=option, y=responses)) 
qh <- qh + geom_bar(binwidth=.5, colour="black", fill="white", stat="identity")
qh <- qh + facet_grid(. ~ question)
qh <- qh + labs(title = quizNumber, x = "Question Option", y = "Number of Responses") 
qh

# Combined plot of daily activity
snapshot <- ggplot(daily_slice, aes(x=item, colour = Activity)) 
snapshot <- snapshot + geom_line(aes(y=registrations, group=session, colour = "New registrations"), size = 1)
snapshot <- snapshot + geom_line(aes(y=quiz_quiz_total, group=session, colour = "Quiz submissions"), size = 1)
snapshot <- snapshot + geom_line(aes(y=lecture_view_total, group=session, colour = "Lecture views"), size = 1)
snapshot <- snapshot + geom_line(aes(y=forum_comment_total+forum_post_total, group=session, colour = "Forum submissions"), size = 1)
snapshot <- snapshot + theme(axis.text.x  = element_text(angle=90, vjust=0.5))
snapshot <- snapshot + labs(title = "Weekly Activity", y="") 
snapshot

# Total lecture activity
lectures <- ggplot(daily_slice, aes(x=item, colour = Activity)) 
lectures <- lectures + geom_line(aes(y=lecture_view_total, group=session, colour = "lecture views"), size = 1)
lectures <- lectures + geom_line(aes(y=lecture_download_total, group=session, colour = "lecture downloads"), size = 1)
lectures <- lectures + theme(axis.text.x  = element_text(angle=90, vjust=0.5))
lectures <- lectures + labs(title = "Lecture Activity", x = "Date", y = "") 
lectures

# Total Forum Posts and Comments
fpc <- ggplot(daily_slice, aes(x=item, group=session, colour = Activity))
fpc <- fpc + geom_line(aes(y=forum_post_total, colour = "Posts"), size = 1)
fpc <- fpc + geom_line(aes(y=forum_comment_total, colour = "Comments"), size = 1)
fpc <- fpc + theme(axis.text.x  = element_text(angle=90, vjust=0.5))
fpc <- fpc + labs(title = "Forum Posts and Comments by Date", x = "Date", y = "") 
fpc

# Quiz Submission by Date
quiz <- ggplot(daily_slice, aes(x=item, y=quiz_quiz_total, group=session)) 
quiz <- quiz + geom_bar(binwidth=.5, colour="black", fill="white", stat="identity")
quiz <- quiz + theme(axis.text.x  = element_text(angle=90, vjust=0.5))
quiz <- quiz + labs(title = "Quiz Submissions by Date", x = "Date", y = "") 
quiz

# Combined plot of weekly activity
weekly_summary <- ggplot(weekly_slice, aes(x=item, colour = Activity))
weekly_summary <- weekly_summary + geom_line(aes(y=registrations, group=session, colour = "New registrations"), size = 1)
weekly_summary <- weekly_summary + geom_line(aes(y=quiz_quiz_total, group=session, colour = "Quiz submissions"), size = 1)
weekly_summary <- weekly_summary + geom_line(aes(y=lecture_view_total, group=session, colour = "Lecture views"), size = 1)
weekly_summary <- weekly_summary + geom_line(aes(y=forum_comment_total+forum_post_total, group=session, colour = "Forum submissions"), size = 1)
weekly_summary <- weekly_summary + labs(title = "Weekly Activity", x = "", y="") 
weekly_summary

# Weekly Forum Posts and Comments
weekly_forum <- ggplot(weekly_slice, aes(x=item, group=session, colour = Activity))
weekly_forum <- weekly_forum + geom_line(aes(y=forum_post_total, colour = "Posts"), size = 1)
weekly_forum <- weekly_forum + geom_line(aes(y=forum_comment_total, colour = "Comments"), size = 1)
weekly_forum <- weekly_forum + labs(title = "Forum Posts and Comments by Date", x = "", y = "") 
weekly_forum

# Weekly lecture activity
weekly_lectures <- ggplot(weekly_slice, aes(x=item, colour = Activity)) 
weekly_lectures <- weekly_lectures + geom_line(aes(y=lecture_view_total, group=session, colour = "lecture views"), size = 1)
weekly_lectures <- weekly_lectures + geom_line(aes(y=lecture_download_total, group=session, colour = "lecture downloads"), size = 1)
weekly_lectures <- weekly_lectures + labs(title = "Lecture Activity", x = "", y = "") 
weekly_lectures
