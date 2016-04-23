#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/32017/dashboard#s=p0
################################################################

import sys

N = int(raw_input());

for t in range(N):
	n, A, B, C, D, x0, y0, M = map(int, raw_input().split());

	bucket = [];
	for i in range(3):
		row = [];
		for j in range(3):
			row.append(0);
		bucket.append(row);

	X = x0;
	Y = y0;

	trees = [];
	trees.append( (X, Y) );
	bucket[X%3][Y%3] += 1;

	for i in range(n-1):
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		trees.append( (X, Y) );
		bucket[X%3][Y%3] += 1;

	result = 0;

	for i in range(3):
		for j in range(3):
			result += (bucket[i][j] * (bucket[i][j]-1) * (bucket[i][j]-2))/6;	# All three vertices are of same type
		result += bucket[i][0] * bucket[i][1] * bucket[i][2];		# All three vertices have same x-type, distinct y-type
		result += bucket[0][i] * bucket[1][i] * bucket[2][i];		# All three vertices have same y-type, distinct x-type
		

	for i in range(3):
		for j in range(3):
			for k in range(3):
				if not(i == j) and not(j == k) and not(k == i):
					result += bucket[0][i] * bucket[1][j] * bucket[2][k];

	print "Case #" + str(t+1) + ":", result;
