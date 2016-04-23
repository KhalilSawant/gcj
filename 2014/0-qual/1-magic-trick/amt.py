#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/2974486/dashboard#s=p0
################################################################

import sys;

T = int(raw_input());

for i in range(T):
	ans_1 = int(raw_input());
	config_1 = [];
	for j in range(4):
		config_1.append(list(map(int,raw_input().split())));

	ans_2 = int(raw_input());
	config_2 = [];
	for j in range(4):
		config_2.append(list(map(int,raw_input().split())));
	
	matches = 0;
	lastmatch = 0;
	for j in range(4):
		for k in range(4):
				if (config_1[ans_1-1][j] == config_2[ans_2-1][k]):
					last_match = config_1[ans_1-1][j];
					matches = matches+1;
	
	if (1 == matches):
		print('Case #%d: %d' % (i+1, last_match) );
	elif (0 == matches):
		print('Case #%d: Volunteer cheated!' % (i+1));
	else:
		print('Case #%d: Bad magician!' % (i+1));
