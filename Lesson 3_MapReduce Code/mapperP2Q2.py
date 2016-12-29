#!/usr/bin/python

'''
mapreduce code to determine number of hits to the site made by each different IP address.

Format of each line is:
IP address\tclient Identity\tClient Username\tRequest Time\tRequest Line\tStatus Code\tReturned object size

For this question we want key (request line) and value 1 

'''

import sys

for line in sys.stdin:
	data = line.strip().split('"GET ')

	if len(data)!=2:
		continue
        
        IPadd = data[0].split(' ')[0]

	print "{0}\t{1}".format(IPadd.strip(),1)
