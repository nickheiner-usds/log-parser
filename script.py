import sys
import re

file = open('fixtures/{}'.format(sys.argv[1]))

date_regex = re.compile('.*\[(2017-\d\d-\d\d \d\d:\d\d:\d\d -0400)\].*')

for line in file:
    date_match = date_regex.match(line)
    if not date_match:
        print 'Line did not match: "{}"'.format(line)
        continue

    date = date_match.group(1)
    print date