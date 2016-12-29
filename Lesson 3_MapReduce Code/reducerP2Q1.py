#!/usr/bin/python

'''
mapreduce Code displaying the number of hits for each different file on the website

this file will receive a key and return the count of one key '/assets/js/the-associates.js' 

'''

import sys

oldKey = None
count = 0

for line in sys.stdin:

	thisKey, thiscount = line.strip('\t')

	if oldkey and olkey!=thisKey:
		print "{0}\t{1}".format(oldkey, count)
                count = 0
	
	oldkey = thisKey
	count +=1

if oldkey:
	print "{0}\t{1}".format(oldkey, count)

