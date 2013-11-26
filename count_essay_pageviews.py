# Samuel Crane
# https://github.com/samuelcrane

import json

def count_pageviews(URL, essay):
    """ (str, str) -> int

    Print the essay and number of pageviews of that essay by counting
    the number of times the essay's URL appears in the pageview events
    in the Coursrea clickstream json file. 

    >>> count_pageviews(json_key, 'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History')
    https://class.coursera.org/amnhgenetics-001/wiki/view?page=Genetics_Short_History
    VIEWS: 4269
    >>> count_pageviews('page_url', 'https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality')
    https://class.coursera.org/amnhgenetics-001/wiki/view?page=Mapping_Morality
    VIEWS: 786
    """
    number_of_pageviews = 0
    with open('amnhgenetics-001_clickstream_export') as f:
        for line in f:
            event = json.loads(line)
            if event[URL] == essay:
                number_of_pageviews += 1
    print essay
    print 'VIEWS:', number_of_pageviews


json_key = 'page_url'

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

for essay in essay_list:
    count_pageviews(json_key, essay)
