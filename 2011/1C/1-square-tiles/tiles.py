#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/1128486/dashboard#s=p0
################################################################

import sys;

T = int(raw_input());

upper_half_tile = str('/\\');
lower_half_tile = str('\\/');

for case in range(T):
	R,C = map(int, raw_input().split());
	
	orig_map = [];
	for row in range(R):
		orig_map.append(raw_input().rstrip());

	impossible = False;
	for row in range(R-1):
		left_top = orig_map[row].find('#');
		while left_top != -1:
			if left_top == C-1:
				impossible = True;
				break;
			elif orig_map[row][left_top+1] != '#' or orig_map[row+1][left_top] != '#' or orig_map[row+1][left_top+1] != '#':			
				impossible = True;
				break;
			else:
				modified_row = orig_map[row][:left_top] + upper_half_tile + orig_map[row][left_top+2:];
				modified_next_row = orig_map[row+1][:left_top] + lower_half_tile + orig_map[row+1][left_top+2:];			
				orig_map[row] = modified_row;
				orig_map[row+1] = modified_next_row;
				left_top = orig_map[row].find('#');
		
		if impossible == True:
			break;

	if not impossible:
		if orig_map[-1].find('#') != -1:
			impossible = True;
	
	print "Case #" + str(case+1) + ":";
	if impossible:
		print "Impossible";
	else:
		for row in range(R):
			print orig_map[row];
