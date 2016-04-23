#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/1145485/dashboard#s=p0
################################################################

import sys;
import math;
import fractions

T = int(raw_input());

for case in range(T):
	input = map(int, raw_input().split());
	
	gcd = fractions.gcd(input[1],100);
	if (100/gcd) > input[0]:
			print "Case #" + str(case+1) + ":",
			print "Broken"
	else:
		if input[2] == 0 or input[2] == 100:
			if (input[2] == input[1]):
				print "Case #" + str(case+1) + ":",
				print "Possible"
			else:
				print "Case #" + str(case+1) + ":",
				print "Broken"
		else:
			print "Case #" + str(case+1) + ":",
			print "Possible"
