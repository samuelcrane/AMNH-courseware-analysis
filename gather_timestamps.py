# Samuel Crane
# https://github.com/samuelcrane
# Reads the JSON serialized clickstream file provided by Coursera and makes a CSV output containing three
# columns: 13-digit POSIX time (milliseconds), 10-digit POSIX time (seconds), datetime (YYYY-MM-DD HH:MM:SS)

import json
import csv
import datetime

def gather_timestamps(clickstream):
    """ (str) -> list
    """
    timestamps = ['timestamps_13']
    with open(clickstream) as f:
        print 'Gathering all timestamps...'
        for line in f:
            event = json.loads(line)
            timestamps.append(event['timestamp'])
        print 'Done.'
    return timestamps

# Specify the location of the JSON-serialized clickstream file provided by Coursera
clickstream = 'amnhgenetics-001_clickstream_export'

times = gather_timestamps(clickstream)

# Change the 13-digit POSIX time to 10-digit POSIX time
times_modified = ['timestamps_10']
for item in times[1:]:
    ten_digit_timestamp = str(item)[:-3]
    times_modified.append(int(ten_digit_timestamp))

# Convert 10-digit POSIX time to datetime
dates = ['datetime']
for item in times_modified[1:]:
    dates.append(datetime.datetime.fromtimestamp(int(item)).strftime('%Y-%m-%d %H:%M:%S'))

print '\nWriting output file...'
rows = zip(times,times_modified,dates)
output_file = open('/Users/sc/Dropbox/data/Genetics/dataexport/output/timestamps.csv', 'w')
datawriter = csv.writer(output_file)
datawriter.writerows(rows)
output_file.close()

print 'All done.'
