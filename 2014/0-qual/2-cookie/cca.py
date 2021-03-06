#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/2974486/dashboard#s=p1
################################################################

import sys;
import math;

T = int(raw_input());

for i in range(T):

	(C,F,X) = list(map(float,raw_input().split()))
	rate = 2;

	if X > C:
		min_rate_req = (X-C)*F/C;
		iterations = int(math.ceil((min_rate_req-rate)/F));
		time = 0;
		for j in range(iterations):
			time = time + (C/rate);
			rate = rate+F;

		time = time + (X/rate);

		print("Case #%d: %.7f" %(i+1,time));
	else:
		print("Case #%d: %.7f" %(i+1,X/rate));
	
