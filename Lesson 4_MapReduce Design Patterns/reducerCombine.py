#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
id_node = None
id_user = None


def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    for line in sys.stdin:
        
        data_mapped = line.strip().split('\t')
        
        # set the id and data for forum_node
        if data_mapped[1] == 'A':
            id_node = data_mapped[0]
            data_node = data_mapped[2:]
            
        # set the id and data for forum_user
        elif data_mapped[1] == 'B':
            id_user = data_mapped[0]
            data_user = data_mapped[2:]
        
        # join forum_user and forum_node if 'user_ptr_id' is equal to 'author_id'
        if id_node == id_user:
            write.writerow(data_user[:3]+[id_user]+data_user[3:]+data_node)
            

