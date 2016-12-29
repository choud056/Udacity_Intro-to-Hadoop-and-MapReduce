#!/usr/bin/python

# Format of each line is:
# weekday\tcost
#
# We want mean of the cost for each weekday
# We need to write them out to standard output, separated by a tab


import sys

oldkey = None
costtotal = 0.0
count = 0

for line in sys.stdin:
	
	data_mapped = line.strip().split('\t')

	if len(data_mapped)!=2:
		continue

	thisday, thiscost = data_mapped

	if oldkey and oldkey!=thisday:
		print "{0}\t{1}".format(oldkey,costtotal*1.0/count)
		costtotal = 0.0
		count = 0
	
	oldkey = thisday
	costtotal+=float(thiscost)
	count+=1

if oldkey!=None:
	print "{0}\t{1}".format(oldkey,costtotal*1.0/count)


