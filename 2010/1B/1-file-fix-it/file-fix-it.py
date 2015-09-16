################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/635101/dashboard#s=p0
################################################################

import sys;
import string;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for i in range(T):
	N, M = map(int, f_ip.readline().split());
	
	present = set();
	
	for j in range(N):		
		path = f_ip.readline().rstrip();
		while len(path):
			present.add(path);
			path, sep, rest = path.rpartition('/');

	needed = 0;
	for j in range(M):
		path = f_ip.readline().rstrip();
		while len(path) and path not in present:
			present.add(path);
			needed += 1;
			path, sep, rest = path.rpartition('/');

	print "Case #" + str(i+1) + ":",
	print needed;
