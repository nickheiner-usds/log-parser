import sys
import re
from datetime import datetime

file = open('fixtures/{}'.format(sys.argv[1]))

# I don't have admin access on this government-issued machine, so I can't install pip. 
# That makes some things weird.
hour_regex = re.compile('.*\[2017-\d\d-\d\d (\d\d):\d\d:\d\d -0400\].*')

count_by_hour = dict({hour: 0 for hour in range(24)})
lines_parsed = 0

for line in file:
    hour_match = hour_regex.match(line)
    if not hour_match:
        print 'Line did not match: "{}"'.format(line)
        continue

    hour = int(hour_match.group(1))
    count_by_hour[hour] += 1

    lines_parsed += 1

    if lines_parsed % 500 == 0:
        print 'Parsed {} lines'.format(lines_parsed)

for hour, count in count_by_hour.iteritems():
    print '{},{}'.format(hour, count)