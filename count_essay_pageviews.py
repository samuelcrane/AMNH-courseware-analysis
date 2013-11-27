# Samuel Crane
# https://github.com/samuelcrane

import json
import csv

def count_total_pageviews(essay, clickstream):
    """ (str, str) -> int

    Opens the clickstream file and parses one line at a time (each
    line in the file is a valid JSON object and corresponds to a user
    event), and counts up the number of pageviews if the event loaded
    the essay URL string.
    
    >>> count_total_pageviews('https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History')
    4269
    >>> count_total_pageviews('https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality')
    786
    """
    number_of_pageviews = 0
    with open(clickstream) as f:
        print 'Counting total pageviews...'
        for line in f:
            event = json.loads(line)
            if event['page_url'] == essay:
                number_of_pageviews += 1
        print 'Done.'
    return number_of_pageviews

def count_unique_pageviews(essay, clickstream):
    """ (str, str) -> int

    Opens the clickstream file and parses one line at a time (each
    line in the file is a valid JSON object and corresponds to a user
    event), and if the event loaded the essay URL string, adds the
    username to a list of unique usernames. If the username is already
    in the list (because the user has already been encountered and was
    previously added to the list), then the event is skipped. Thus, the
    length of the unique username list is the number of unique pageviews

    >>> count_unique_pageviews('https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History')
    2245
    >>> count_unique_pageviews('https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality')
    565
    """
    unique_users = []
    with open(clickstream) as f:
        print 'Counting unique pageviews...'
        for line in f:
            event = json.loads(line)
            if event['page_url'] == essay and event['username'] not in unique_users:
                unique_users.append(event['username'])
        print 'Done.'
    unique_pageviews = len(unique_users)
    return unique_pageviews

essay_list = [
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
'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality'
]

# Specify the location of the JSON-serialized clickstream file provided by Coursera
clickstream = 'amnhgenetics-001_clickstream_export'

# Initialize list for CSV output and specify header names
essay_pageviews = [['essay_title','total_views','unique_views','average_views','essay_url']]

# Process all the essays
for essay in essay_list:
    essay_title = essay.replace('https://class.coursera.org/amnhgenetics-001/wiki/view?page=', '').replace('_', ' ')
    print '\nEssay:', essay_title
    total = count_total_pageviews(essay, clickstream)
    unique = count_unique_pageviews(essay, clickstream)
    average_visits = format(total/float(unique), '.2f')
    essay_pageviews.append([essay_title,total,unique,average_visits,essay])

print '\nWriting output file...'
output_file = open('essay_pageviews.csv', 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(essay_pageviews)
output_file.close()

print 'Finished counting essay page views.'
