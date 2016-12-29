#!/usr/bin/python

# Input file contains node_id , node_type and body
# We want the node_id, question_length and avg_answer_length as the output of our reducer

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
writer = csv.writer(sys.stdout,delimiter='\t')

oldkey = None
answer_total_length = 0
answer_count = 0
question_length = 0

# setting header for writer
writer.writerow(['Question Node ID |','Question Length |','Average Answer Length'])

for line in reader:

	if len(line)!=3:
		continue

	node_id = int(line[0])

	str_node_type_list = ['question','answer']
	node_type = str_node_type_list[int(line[1])]

	len_body = int(line[2])
	

	# Giving output only when new node is question (since all the previous nodes are answers to the previous question)
	if oldkey and oldkey!=node_id and node_type == 'question':
		if answer_count==0:	
			writer.writerow([oldkey,question_length,0])
		else:
			writer.writerow([oldkey,question_length,answer_total_length*1.0/answer_count])
		question_length = 0
		answer_count = 0
		answer_total_length = 0
		
	oldkey = node_id

        # checking if node_type is question
	if node_type == 'question':
		question_length = len_body

	# checking if node_type in answer
	if node_type == 'answer':
		answer_total_length+=len_body
		answer_count+=1

# To get output of the final key
if oldkey and question_length!=None and node_type=='question':
		if answer_count==0:	
			writer.writerow([oldkey,question_length,0])
		else:
			writer.writerow([oldkey,question_length,answer_total_length*1.0/answer_count])
