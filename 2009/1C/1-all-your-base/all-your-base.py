#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/189252/dashboard#s=p0
################################################################

import sys;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for i in range(T):
	msg = f_ip.readline().rstrip();
	msg_sz = len(msg);
	chars = set();
	for j in msg:
		chars.add(j);
	radix = max(2, len(chars));

	value_map = dict();
	value_map[msg[0]] = 1;
	chars.remove(msg[0]);
	for j in msg:
		if j in chars:
			value_map[j] = 0;
			chars.remove(j);
			break;
	value = 2;
	for j in msg:
		if j in chars:
			value_map[j] = value;
			value += 1;
			chars.remove(j);
	time = 0;
	for j in msg:
		time *= radix;
		time += value_map[j] ;
		
	print "Case #" + str(i+1) + ":",
	print time;
