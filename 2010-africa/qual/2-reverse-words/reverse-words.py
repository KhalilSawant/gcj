#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/351101/dashboard#s=p1
################################################################

import sys

f_ip = open(sys.argv[1], 'r');
N = int(f_ip.readline());
for i in range(N):
	line = f_ip.readline();
	word_list = line.split();
	word_list.reverse();
	print "Case #" + str(i+1) + ":",
	for word in word_list:
		print word,
	print "";
