################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/837485/dashboard#s=p0
################################################################

import sys

f_ip = open(sys.argv[1], 'r');
N = int(f_ip.readline());
for i in range(N):
	f_ip.readline();
	segments = f_ip.readline().split();
	blue = [];
	red = [];
	for j in segments:
		if j[-1] == 'B':
			blue.append(int(j[:-1]));
		else:
			red.append(int(j[:-1]));

	blue.sort();
	blue.reverse();
	red.sort();
	red.reverse();
	
	count = min(len(blue),len(red));
	
	if count == len(blue):
		for j in range(len(red) - count):
				red.pop();
	else:
		for j in range(len(blue) - count):
				blue.pop();

	final_total = sum(red);
	final_total += sum(blue);
	
	final_total -= (2*count)
	
	print "Case #" + str(i+1) + ":",	
	print final_total;