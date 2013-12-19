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

# List of page URLS for course essays
essay_URLS = [
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Nature_Nurture',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Thinking_Ethically',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Advancing_Technology',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Cloning_How_Why',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Tools_Techniques',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=DNA_Fingerprinting',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Epigenetics_Epigenome',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Human_Variation',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Redesigning_Self',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetic_Testing_Conundrum',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genomics_Biotechnology_Agriculture',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=BT_Corn',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality']

# Define lists for output columns
summarized_usernames = ['username']
summarized_sessions = ['session']
summarized_essays = ['page_url']
dates = ['date']
durations = ['seconds']

# This is an arbitrary length of time (seconds) after which no reasonable
# person could be assumed to still be on task.
# For example, it's unreasonable to think that someone spent an hour reading
# a 900 word essay that should take a native reader about 5 minutes to read.
inactivity_threshold = 3600

rowID = 1
sessionID = clickstream[rowID][2]

print '\nAnalyzing essay data...'
while rowID < len(clickstream):
    # Find page view events on essay page URLs
    if clickstream[rowID][3] == 'pageview' and clickstream[rowID][9] in essay_URLS:
        essay = clickstream[rowID][9]
        start_time = clickstream[rowID][6]
        within_session_rowID = rowID
        
        # Cycle through this viewing session
        while clickstream[within_session_rowID][9] == essay: 
            within_session_rowID += 1
            # Break if too much time has passed between events (inactivity threshold has been met)
            elapsed_time = int(clickstream[within_session_rowID][6]) - int(clickstream[within_session_rowID - 1][6])
            if elapsed_time > inactivity_threshold:
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
            summarized_essays.append(clickstream[within_session_rowID - 1][9])
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
            summarized_essays.append(clickstream[within_session_rowID - 1][9])
            dates.append(clickstream[within_session_rowID - 1][8])
            durations.append(duration)
            
        rowID +=1
    rowID +=1
print 'Done.'


# Process essays titles
titles = ['title']
for essay in summarized_essays[1:]:
    essay_title = essay.replace('https://class.coursera.org/amnhgenetics-001/wiki/view?page=', '').replace('_', ' ')
    titles.append(essay_title)

# Assign Week
weeks = ['week']
Week_1 = [
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Nature_Nurture',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Thinking_Ethically',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Advancing_Technology']
Week_2 = [
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Cloning_How_Why',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Tools_Techniques',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=DNA_Fingerprinting']
Week_3 =[
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Epigenetics_Epigenome',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Human_Variation',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Redesigning_Self',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetic_Testing_Conundrum']
Week_4 = [
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genomics_Biotechnology_Agriculture',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=BT_Corn',
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality']
for essay in summarized_essays[1:]:
    if essay in Week_1:
        weeks.append('1')
    elif essay in Week_2:
        weeks.append('2')
    elif essay in Week_3:
        weeks.append('3')
    elif essay in Week_4:
        weeks.append('4')



print '\nWriting output file...'
rows = zip(titles,weeks,summarized_usernames,summarized_sessions,dates,durations,summarized_essays)
output_file = open('essay_summary.csv', 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(rows)
output_file.close()
print 'Finished.'
