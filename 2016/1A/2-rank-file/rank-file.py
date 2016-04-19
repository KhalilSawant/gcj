#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/433101/dashboard#s=p1
################################################################

import sys;

T = int(raw_input());

for i in range(T):

	N = int(raw_input().strip());

	numbers = [];

	for j in range(2*N-1):
		numbers.extend(map(int, raw_input().strip().split()));

	numbers.sort();

	outliers = [];
	j = 0;
	while j < len(numbers)-1:
		if numbers[j] != numbers[j+1]:
			outliers.append(numbers[j]);
			j = j+1;
		else:
			j = j+2;

	if j == len(numbers)-1:
		outliers.append(numbers[-1]);

	print("Case #%d: %s" %(i+1, " ".join(map(str, outliers)) ) );
