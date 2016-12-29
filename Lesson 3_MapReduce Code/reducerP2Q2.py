#!/usr/bin/python

'''
mapreduce code to determine number of hits to the site made by each different IP address.

this file will receive a key and return the count of one keys

'''

import sys

count = 0
oldkey = None

for line in sys.stdin:

	thisKey,thiscount = line.strip('\t')

	if oldkey and oldkey!=thisKey:
		print "{0}\t{1}".format(oldkey,count)
		count = 0
	
	oldkey = thisKey	
	count +=1

if oldkey:
	print "{0}\t{1}".format(oldkey,count)
