################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/433101/dashboard#s=p1
################################################################

import sys;
from collections import deque;
from operator import __sub__;
from fractions import gcd;

f_ip = open(sys.argv[1], 'r');
C = int(f_ip.readline());

for i in range(C):
	t = deque( map( int, f_ip.readline().split() ) );
	N = t.popleft(); # deque contains no of items as object[0]

	pivot = t[0];
	difference = [abs(x-pivot) for x in t];

	T = reduce(gcd, difference);

	if pivot % T == 0:
		result = 0;
	else:
		result = T - (pivot % T);
	print "Case #" + str(i+1) + ": " + str(result);
