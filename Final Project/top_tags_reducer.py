#!/usr/bin/python

# Input file contains tag , count(tag)
# We want the top 10 tags and total count of those tag

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

oldtag = None
tag_count = 0
tag_and_count_list = []

# setting header for writer
writer.writerow(['Tag','Counts'])

for line in reader:

	if len(line)!=2:
		continue

	thistag, thiscount = line

	if oldtag and oldtag!=thistag:
		tag_and_count_list.append([tag_count,oldtag])
		tag_count = 0
	
	oldtag = thistag
	tag_count+=1

if oldtag:
	tag_and_count_list.append([tag_count,oldtag])

tag_and_count_list.sort(reverse=True)

for count, tag in tag_and_count_list[:10]:
	writer.writerow([tag,count])



