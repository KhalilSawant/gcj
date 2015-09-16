################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/32016/dashboard#s=p0
################################################################

import sys;
from operator import mul;

f_ip = open(sys.argv[1], 'r');
T = int(f_ip.readline());

for i in range(T):
	f_ip.readline();
	vect_str_1 = f_ip.readline().split();
	vect_str_2 = f_ip.readline().split();

	vect_1 = map(int, vect_str_1);
	vect_2 = map(int, vect_str_2);
	
	vect_1.sort();
	vect_2.sort();
	vect_2.reverse();

	vect_prod = map(mul, vect_1, vect_2);

	print "Case #" + str(i+1) + ": " + str(sum(vect_prod));
