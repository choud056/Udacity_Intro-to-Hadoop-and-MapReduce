#!/usr/bin/python


# Extract all the words from the forum_node file


import sys
import re

for line in sys.stdin:

	data = line.strip().split('\t')
	
	if len(data)==19 and data[0]!='"id"':
		node = re.sub('"','',data[0])
		body = data[4]
      		words = re.split('[\s"\.#,[!?\](:)$<>=/\-;]',body)  
		
		for word in words:
			if len(word)>1 and word.isalpha():
				print "{0}\t{1}".format(word.lower(),int(node))

