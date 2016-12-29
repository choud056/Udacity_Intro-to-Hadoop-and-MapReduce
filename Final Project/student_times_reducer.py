#!/usr/bin/python

# Input file is in format key (author_id) and value (hour_added) (the hour when author added a post)

# We want reducer to return author_id and the hour for which the author has posted most posts

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

# Add a header to the output file [author_id\thour_max_posts]
writer.writerow(['author_id','hour_max_posts'])

hourcounts = []
hourlist = []
oldkey = None

for line in reader:

	data_mapped = line
	
	if len(data_mapped)!=2:
		continue
	
	thiskey, thishour = data_mapped
	
 	# when the new key arrives print the old one and maximum posted hour
	if oldkey and oldkey!=thiskey:
		max_count = max(hourcounts)

		# all the indexes for which the hours spent posting are maximum
		max_ind = [idx for idx,count in enumerate(hourcounts) if count==max_count]

		for i in max_ind:
			writer.writerow([oldkey,hourlist[i]])

		# re-initialize the lists for new key
		hourlist = []
		hourcounts = []
	
	oldkey = thiskey
	
	if thishour in hourlist:
		idx = hourlist.index(thishour)
		hourcounts[idx]+=1
	else:
		hourlist.append(thishour)
		hourcounts.append(1)
	
# To take the last key's output
if oldkey:
	max_count = max(hourcounts)
	# all the indexes for which the hours spent posting are maximum
	max_ind = [idx for idx,count in enumerate(hourcounts) if count==max_count]

	for i in max_ind:
		writer.writerow([oldkey,hourlist[i]])

	
	

	

	
	
