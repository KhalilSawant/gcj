#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/351101/dashboard#s=p0
################################################################

import sys

N = int(raw_input());
for i in range(N):
	C = int(raw_input());
	I = int(raw_input());
	line = raw_input();
	str_list = line.split();
	price_list = [];
	iter = 0;
	for j in str_list:
		price_list.append((int(j),iter));
		iter = iter+1;
	price_list.sort();
	
	l_ptr = 0;
	r_ptr = I-1;
	while l_ptr < r_ptr:
		if price_list[l_ptr][0]+price_list[r_ptr][0] == C:
			if price_list[l_ptr][1] < price_list[r_ptr][1]:
				print "Case #" + str(i+1) + ": " + str(price_list[l_ptr][1]+1) + " " + str(price_list[r_ptr][1]+1);
			else:
				print "Case #" + str(i+1) + ": " + str(price_list[r_ptr][1]+1) + " " + str(price_list[l_ptr][1]+1);
			break;
		elif price_list[l_ptr][0]+price_list[r_ptr][0] < C:
			l_ptr = l_ptr+1;
		else:
			r_ptr = r_ptr-1;
