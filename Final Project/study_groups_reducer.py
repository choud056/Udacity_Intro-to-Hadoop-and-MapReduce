#!/usr/bin/python

'''
STUDY GROUP PROBLEM

We want ot see if there are students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that 
is a question node with all it's answers and comments) would give us a list of students that have posted there - either
asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

'''

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

oldkey = None
author_ids = []

for line in reader:

	if len(line)!=2:
		continue

	node_id , author_id = line

	if oldkey and oldkey!=node_id:
		writer.writerow([oldkey, author_ids])
		author_ids = []

	oldkey = node_id

	author_ids.append(int(author_id))

if oldkey:
	writer.writerow([oldkey, author_ids])


