#!/usr/bin/python

# Input file contains author_id and date when the author added a post
# We want the element 3 (author_id) and element 8 (added_at) as the output of our mapper

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

# skip the header
reader.next()


for line in reader:


	if len(line)!=19:
		continue
	
	author_id = line[3]

	date_added = line[8].split('.')[0] 

	hour_added = datetime.strptime(date_added, "%Y-%m-%d %H:%M:%S").hour

	writer.writerow([author_id, hour_added])

	
	
