# Samuel Crane
# http://www.samuelcrane.com
# https://github.com/samuelcrane
#
# R code
# Updated: 2013-09-27
# Time Series plots for weekly or daily activity data from Coursera MOOC data
# Transpose the CSV file before reading it. 

library('ggplot2')

# Read in and parse daily activity
# Before this step, I've transposed the CSV file that Coursera provides under the Activity->Daily download.
daily <- read.csv("/Week3/plot/input/daily.csv")

# Subset the data by a week or a few days
daily_slice <- daily[149:152,]
daily_slice <- cbind(daily_slice, session = "amnhgenetics001")

# Combined plot of weekly activity
snapshot <- ggplot(daily_slice, aes(x=item, colour = Activity)) 
snapshot <- snapshot + geom_line(aes(y=registrations, group=session, colour = "registrations"), size = 1)
snapshot <- snapshot + geom_line(aes(y=quiz_quiz_total, group=session, colour = "quiz"), size = 1)
snapshot <- snapshot + geom_line(aes(y=lecture_view_total, group=session, colour = "lectures"), size = 1)
snapshot <- snapshot + geom_line(aes(y=forum_comment_total+forum_post_total, group=session, colour = "forum"), size = 1)
snapshot <- snapshot + labs(title = "Weekly Activity", y="") 
snapshot

# Total lecture activity
lectures <- ggplot(daily_slice, aes(x=item, colour = Activity)) 
lectures <- lectures + geom_line(aes(y=lecture_view_total, group=session, colour = "lecture views"), size = 1)
lectures <- lectures + geom_line(aes(y=lecture_download_total, group=session, colour = "lecture downloads"), size = 1)
lectures <- lectures + labs(title = "Lecture Activity", x = "Date", y = "") 
lectures

# Total Forum Posts and Comments
fpc <- ggplot(daily_slice, aes(x=item, group=session, colour = Activity))
fpc <- fpc + geom_line(aes(y=forum_post_total, colour = "Posts"), size = 1)
fpc <- fpc + geom_line(aes(y=forum_comment_total, colour = "Comments"), size = 1)
fpc <- fpc + labs(title = "Forum Posts and Comments by Date", x = "Date", y = "") 
fpc

# Quiz Submission by Date
quiz <- ggplot(daily_slice, aes(x=item, y=quiz_quiz_total, group=session)) 
quiz <- quiz + geom_bar(binwidth=.5, colour="black", fill="white", stat="identity")
quiz <- quiz + labs(title = "Total Quiz Submissions by Date", x = "Date", y = "Quiz Submissions") 
quiz
