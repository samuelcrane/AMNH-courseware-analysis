# Samuel Crane
# https://github.com/samuelcrane

# Experimental

import csv

# Read ordered CSV of clickstream data into a list
print 'Reading in clickstream data...'
clickstreamfile = open('all_sessions_ordered.csv', 'r')
reader = csv.reader(clickstreamfile)
clickstream = []
for row in reader:
    clickstream.append(row)

# List of page URLS for course videos
video_URLS = [
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=25',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=27',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=29',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=31',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=3',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=33',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=35',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=43',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=37',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=15',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=17',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=19',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=47',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=39',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=41',
'https://class.coursera.org/amnhgenetics-001/lecture/view?lecture_id=49']

# Define lists for output columns
summarized_usernames = ['username']
summarized_sessions = ['session']
summarized_videos = ['page_url']
dates = ['date']
durations = ['seconds']

# This is an arbitrary length of time (seconds) after which no reasonable
# person could be assumed to still be on task.
# For example, if the activity is PAUSE, and the next activity is PLAY
# and the time between these events is 30 minutes, we can assume that
# this user was not on task during that time by taking notes, etc. 
inactivity_threshold = 300

rowID = 1
sessionID = clickstream[rowID][2]

print '\nAnalyzing video data...'
while rowID < len(clickstream):
    # Find page view events on video page URLs
    if clickstream[rowID][3] == 'pageview' and clickstream[rowID][9] in video_URLS:
        video = clickstream[rowID][9]
        start_time = clickstream[rowID][6]
        within_session_rowID = rowID
        
        # Cycle through this viewing session
        while clickstream[within_session_rowID][9] == video: 
            within_session_rowID += 1
            # Break if too much time has passed between events (inactivity threshold has been met)
            elapsed_time = int(clickstream[within_session_rowID][6]) - int(clickstream[within_session_rowID - 1][6])
            if elapsed_time > inactivity_threshold and clickstream[within_session_rowID - 1][4] != 'play':
                break
            
        same_session = clickstream[within_session_rowID][2] == clickstream[within_session_rowID - 1][2]
        same_day = clickstream[within_session_rowID][8] == clickstream[within_session_rowID - 1][8]
        elapsed_time = int(clickstream[within_session_rowID][6]) - int(clickstream[within_session_rowID - 1][6])

        if same_session and same_day and elapsed_time < inactivity_threshold:
            # Calculate end_time based on timestamp of the user's next event outside of viewing session 
            end_time = clickstream[within_session_rowID][6]
            duration = int(end_time) - int(start_time)
            summarized_usernames.append(clickstream[within_session_rowID - 1][1])
            summarized_sessions.append(clickstream[within_session_rowID - 1][2])
            summarized_videos.append(clickstream[within_session_rowID - 1][9])
            dates.append(clickstream[within_session_rowID - 1][8])
            durations.append(duration)
        else:
            # Calculate end_time based on previous event start time
            # Necessary to avoid anomolous session durations across days and hours of inactivity
            # Artifically depresses duration time but there is no way around this
            end_time = clickstream[within_session_rowID - 1][6]
            duration = int(end_time) - int(start_time)
            summarized_usernames.append(clickstream[within_session_rowID - 1][1])
            summarized_sessions.append(clickstream[within_session_rowID - 1][2])
            summarized_videos.append(clickstream[within_session_rowID - 1][9])
            dates.append(clickstream[within_session_rowID - 1][8])
            durations.append(duration)
            
        rowID +=1
    rowID +=1
print 'Done.'

print '\nWriting output file...'
rows = zip(summarized_usernames,summarized_sessions,dates,durations,summarized_videos)
output_file = open('video_summary.csv', 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(rows)
output_file.close()
print 'Finished.'
