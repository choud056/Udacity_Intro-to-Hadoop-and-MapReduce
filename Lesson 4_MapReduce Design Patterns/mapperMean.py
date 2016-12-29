#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 0 (date) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

from datetime import datetime

for line in sys.stdin:
	
	data = line.strip().split('\t')

	if len(data)!=6:
		continue

	date, time, store, item, cost, payment = data

	weekday = datetime.strptime(date,"%Y-%m-%d").weekday()

	str_weekday = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

	print "{0}\t{1}".format(str_weekday[weekday],cost)
