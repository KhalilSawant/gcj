#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/32015/dashboard#s=p0
################################################################

import sys;

N = int(raw_input());

for i in range(N):
	P, K, L = map(int, raw_input().split() );	
	frequencies = map(int, raw_input().split() );
	frequencies.sort();

	result = 0;
	press_count = 0;

	while len(frequencies) > 0:
		press_count += 1;
		for j in range(K):
			if len(frequencies) > 0:
				frequency = frequencies.pop();
				result += (press_count*frequency);
			else:
				break;
	print "Case #" + str(i+1) + ": " + str(result);

