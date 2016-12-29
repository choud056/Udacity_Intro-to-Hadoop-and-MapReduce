#!/usr/bin/python


# For this reducer will receive words as key and node_id as value 
# and need to return counts of every word and the list of node_ids of the key

import sys

oldkey = None
count = 0
nodes = []

for line in sys.stdin:
	
	data_mapped = line.strip().split('\t')
	
	if len(data_mapped)!=2:
		continue

	thiskey, thisnode = data_mapped
	
	
	if oldkey and oldkey!=thiskey:
		print "{0}\t{1}\t{2}".format(oldkey,count,nodes)
		count = 0
		nodes = []
	
	oldkey = thiskey
	count+=1
	nodes.append(int(thisnode))

if oldkey:
	print "{0}\t{1}\t{2}".format(oldkey,count,nodes) 

