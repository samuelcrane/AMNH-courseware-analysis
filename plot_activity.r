# Samuel Crane
# http://www.samuelcrane.com
# https://github.com/samuelcrane
#
# R code
# Updated: 2013-09-19
# Time Series plots for weekly or daily activity data from Coursera MOOC data
# Transpose the CSV file before reading it. 

# Read in time series activity data
daily <- read.csv("week1/daily_week1.csv")

# Create group column (or do it in Excel)
daily <- cbind(daily, session = "amnhgenetics001")

# Unique forum posts and comments
fcq <- ggplot(daily, aes(x=date, y=forum_combined_unique, group=session)) + geom_line()
fcq <- fcq + labs(title = "Individual People Visitng the Forum") 
fcq

# Total forum posts and comments
fct <- ggplot(daily, aes(x=date, y=forum_combined_total, group=session)) + geom_line()
fct <- fct + labs(title = "Total Forum Activity by Date") 
fct

# Total lecture views and downloads
lct <- ggplot(daily, aes(x=date, y=lecture_combined_total, group=session)) + geom_line()
lct <- lct + labs(title = "Total Video Views and Downloads") 
lct

# Total lecture views
lvt <- ggplot(daily, aes(x=date, y=lecture_view_total, group=session)) + geom_line()
lvt <- lvt + labs(title = "Total Video Views") 
lvt

# Unique lecture views
lvu <- ggplot(daily, aes(x=date, y=lecture_view_unique, group=session)) + geom_line()
lvu <- lvu + labs(title = "Unique Video Views") 
lvu

# Total of all quiz submissions
q1t <- ggplot(daily, aes(x=date, y=quiz_quiz_total, group=session)) + geom_line()
q1t <- q1t + labs(title = "Total Quiz 1 Submissions by Date") 
q1t

# Histogram of all quiz submissions
q1th <- ggplot(daily, aes(x=date, y=quiz_quiz_total, group=session)) 
q1th <- q1th + geom_histogram(binwidth=.5, colour="black", fill="white", stat="identity")
q1th <- q1th + labs(title = "Total Quiz 1 Submissions by Date", x = "Date", y = "Quiz Submissions") 
q1th

# Unique quiz submissions
q1u <- ggplot(daily, aes(x=date, y=quiz_quiz_unique, group=session)) + geom_line()
q1u <- q1u + labs(title = "Individual Quiz Submissions by date") 
q1u

# Registrations
reg <- ggplot(daily, aes(x=date, y=registrations, group=session)) + geom_line()
reg <- reg + labs(title = "Week 1 Registrations per Day") 
reg
