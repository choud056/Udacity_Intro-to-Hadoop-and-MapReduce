#!/usr/bin/python

# Input file contains information of udacity student discussion form
# We are interested to see what are the top tags used in posts
# We want the element 2 (tagnames) and element 5 (node_type) as the output of our mapper,
# where tagnames is the key for the reducer and 1 is the value

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

# skip the header
reader

for line in reader:
	
	if len(line)!=19:
		continue

	tagnames = line[2].split()
	node_type = line[5]

	if node_type == 'question':
		
		for tag in tagnames:
			writer.writerow([tag, 1])
