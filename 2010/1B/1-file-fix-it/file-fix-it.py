#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/635101/dashboard#s=p0
################################################################

import sys;
import string;

T = int(raw_input());

for i in range(T):
	N, M = map(int, raw_input().split());
	
	present = set();
	
	for j in range(N):		
		path = raw_input().rstrip();
		while len(path):
			present.add(path);
			path, sep, rest = path.rpartition('/');

	needed = 0;
	for j in range(M):
		path = raw_input().rstrip();
		while len(path) and path not in present:
			present.add(path);
			needed += 1;
			path, sep, rest = path.rpartition('/');

	print "Case #" + str(i+1) + ":",
	print needed;
