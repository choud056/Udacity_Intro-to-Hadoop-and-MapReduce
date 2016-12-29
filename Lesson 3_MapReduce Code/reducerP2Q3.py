#!/usr/bin/python

'''

reducer outputs the file's path (key) and the number of times it appears in the log

Format of each line is:
IP address\tclient Identity\tClient Username\tRequest Time\tRequest Line\tStatus Code\tReturned object size

'''

import sys
oldKey = None
count = 0
oldcount = 0

for line in sys.stdin:
	data_mapped = line.strip('\t')
	
	thisPath,thiscount = data_mapped

	if oldKey and oldKey!=thisPath:
		if count>oldcount:
			print "{0}\t{1}".format(oldKey, count)
			oldcount = count
	 	count = 0

	oldKey = thisPath
	count += 1

if oldKey!=None:
	if count>oldcount:
		print "{0}\t{1}".format(oldKey, count) 

		

