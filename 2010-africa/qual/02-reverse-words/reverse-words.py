########################################
#	Author:	Khalil Sawant
########################################

import sys

f_ip = open(sys.argv[1], 'r');
N = int(f_ip.readline());
for i in range(N):
	line = f_ip.readline();
	word_list = line.split();
	word_list.reverse();
	print "Case #" + str(i+1) + ":",
	for word in word_list:
		print word,
	print "";
