#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/351101/dashboard#s=p2
################################################################

import string
import sys

char_to_num_hash = [];
for i in range(2,10):
	for j in range(3):
		char_to_num_hash.append(i);
char_to_num_hash.insert(15, 7);
char_to_num_hash.insert(22, 9);

num_to_char_hash = [];
for i in range(10):
	num_to_char_hash.append([]);
num_to_char_hash[0].append(' ');

for c in string.ascii_lowercase:
	pos = string.ascii_lowercase.index(c);
	char_list = num_to_char_hash[char_to_num_hash[pos]];
	char_list.append(c);

N = int(raw_input());

for i in range(N):
	line = raw_input();
#	line = line.rstrip();
	result = "";
	prev_key = 1;
	for c in line:
		if c != ' ':
			pos = string.ascii_lowercase.index(c);
			curr_key = char_to_num_hash[pos];
		else:
			curr_key = 0;

		if curr_key == prev_key:
			result = result+' ';
		press_count = num_to_char_hash[curr_key].index(c);
		for j in range(press_count+1):
			result = result+str(curr_key);
		prev_key = curr_key;

	print "Case #" + str(i+1) + ": " + result;
