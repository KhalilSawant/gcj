########################################
#	Author:	Khalil Sawant
########################################

import sys;

f_ip = open(sys.argv[1], 'r');
N = int(f_ip.readline());

for i in range(N):
	P, K, L = map(int, f_ip.readline().split() );	
	frequencies = map(int, f_ip.readline().split() );
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

