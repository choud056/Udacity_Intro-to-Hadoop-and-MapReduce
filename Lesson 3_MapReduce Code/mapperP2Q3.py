#!/usr/bin/python

'''

mapreduce code for finding the most popular file on the webside: that is, the file whose path occurs most often in access_log.

Format of each line is:
IP address\tclient Identity\tClient Username\tRequest Time\tRequest Line\tStatus Code\tReturned object size

For this question we want key (request line) and value 1'''

import sys
import re

for line in sys.stdin:
	data = line.strip()
	RequestLine = re.findall('".+"',data)[0]
	webpath = re.findall('/\S+\s',RequestLine)
	if len(webpath)!=0:
		webpathModified = re.sub('//www.the-associates.co.uk','',webpath[0])
		print "{0}\t{1}".format(webpathModified.strip(),1)

