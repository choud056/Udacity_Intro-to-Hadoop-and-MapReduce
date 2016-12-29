# Introduction to Hadoop and MapReduce

This repository contains assignment projects from Intro to Hadoop and MapReduce course on Udacity.

A. **Lesson 3_MapReduce Code** contains mapper and reducer codes for access_log data using python.
access_log input data set is an anonymized Web server log file from a public relatios company whose clients were DVD distributers.

mapper and reducer codes for this file solves following problems:

1. **P2Q1** Mapreduce program to display the number of hits for each different file on the website.
2. **P2Q2** Mapreduce program to display the number of hits to the site made by each different IP address
3. **P2Q3** Mapreduce program to display the most popular file on the website

B. **Lesson 4_MapeReduce Design Patterns** includes mapper and reducer codes for implementing mapreduce design patterns:- filtering 
patterns, summarization patterns and structural patterns.

C. **Final Project** includes the mapper and reducer code files to work with discussion forum (also sometimes called discussion board) data. 
It is one type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things that I did in this project
can transfer to other similar projects.

The dataset for this final project is taken from Udacity forums the first months after launch. 
Udacity forums are run on free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.

Using the above discussed data set I answered the following questions in the final project:

1. **student_times** : Display for each student what is the hour during which the student has posted the most posts.
2. **post_answer_length** : Determine if there is a correlation between the length of a post and length of answers.
3. **top_tags** : What are the top tags used in posts.
4. **study_groups** : If there are students on forum that communicate a lot between themselves.

Additional details about all the other files is included in the code itself 




