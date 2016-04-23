#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/351101/dashboard#s=p1
################################################################

import sys

N = int(raw_input());

for i in range(N):
	line = raw_input();
	word_list = line.split();
	word_list.reverse();
	print "Case #" + str(i+1) + ":",
	for word in word_list:
		print word,
	print "";
