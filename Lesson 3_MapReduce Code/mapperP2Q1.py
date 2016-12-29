#!/usr/bin/python

''' 
Project 3 Part 1

mapreduce Code displaying the number of hits for each different file on the website

Format of each line is:
 IP address\tclient Identity\tClient Username\tRequest Time\tRequest Line\tStatus Code\tReturned object size

For this question we want key (request line)

'''
import sys

for line in sys.stdin:
	data = line.strip().split('"GET ')

	if len(data)!=2:
		continue

	if len(data[1].split(' '))!=4:
		continue
        
        RequestLine, http, StatusCode, ObjSize = data[1].split(' ')

	print "{0}\t{1}".format(RequestLine.strip(),1)
