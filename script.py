import sys
import re
from datetime import datetime

file = open('fixtures/{}'.format(sys.argv[1]))

# I would like to include %z when parsing the time zone, but that 
# requires installing additional packages, and I don't have admin 
# access on this government-issued machine, so I can't install pip. 
# I will have to fix the timezone manually.
date_regex = re.compile('.*\[(2017-\d\d-\d\d \d\d:\d\d:\d\d) -0400\].*')

for line in file:
    date_match = date_regex.match(line)
    if not date_match:
        print 'Line did not match: "{}"'.format(line)
        continue

    date_str = date_match.group(1)
    unix_timestamp = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S').strftime('%s')

    print parsed_date