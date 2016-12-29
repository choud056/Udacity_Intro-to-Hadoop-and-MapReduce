#!/usr/bin/python

# Input file contains information of udacity student discussion form
# We are interested to see if there is any correlation between the length of a post and the length of answers
# We want the element 0 (node_id), element 4 (body) and element 5 (node_type) as the output of our mapper,
# where node_id is the key for the reducer

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

# skip the header
reader

for line in reader:
	
	if len(line)!=19:
		continue

	node_id = line[0]
	body = line[4]
	node_type = line[5]

	if node_type == 'question':
		writer.writerow([node_id,0,len(body)])

	elif node_type == 'answer':
		writer.writerow([node_id,1,len(body)])
