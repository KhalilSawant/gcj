#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/433101/dashboard#s=p1
################################################################

import sys;
from collections import deque;
from operator import __sub__;
from fractions import gcd;

C = int(raw_input());

for i in range(C):
	t = deque( map( int, raw_input().split() ) );
	N = t.popleft(); # deque contains no of items as object[0]

	pivot = t[0];
	difference = [abs(x-pivot) for x in t];

	T = reduce(gcd, difference);

	if pivot % T == 0:
		result = 0;
	else:
		result = T - (pivot % T);
	print "Case #" + str(i+1) + ": " + str(result);
