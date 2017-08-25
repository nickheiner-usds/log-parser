import sys
import re
from datetime import datetime

file = open('fixtures/{}'.format(sys.argv[1]))

# I don't have admin access on this government-issued machine, so I can't install pip. 
# That makes some things weird.

hour_regex = re.compile('.*\[2017-\d\d-\d\d (\d\d):\d\d:\d\d -0400\].*')

pathname_regex = re.compile('.*Started GET "([^"]+)".*')

count_by_hour = dict({hour: {'appeals_status': 0, 'caseflow': 0} for hour in range(24)})
lines_parsed = 0

for line in file:
    hour_match = hour_regex.match(line)
    if not hour_match:
        print 'Line did not match hour regex: "{}"'.format(line)
        continue

    pathname_match = pathname_regex.match(line)

    if not pathname_match:
        print 'Line did not match pathname regex: "{}"'.format(line)
        continue

    pathname = pathname_match.group(1)

    appeals_status = pathname == '/api/v1/appeals'

    hour = int(hour_match.group(1))
    key = 'appeals_status' if appeals_status else 'caseflow'
    count_by_hour[hour][key] += 1

    lines_parsed += 1

    if lines_parsed % 500 == 0:
        print 'Parsed {} lines'.format(lines_parsed)

print 'hour,caseflow,appeals_status'
for hour, counts in count_by_hour.iteritems():
    print '{},{},{}'.format(hour, counts['caseflow'], counts['appeals_status'])