#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/4304486/dashboard#s=p0
################################################################

import sys;

T = int(raw_input());

for i in range(T):

	inputStr = raw_input().strip();

	outputStr = inputStr[0];

	for char in inputStr[1:]:
		if char >= outputStr[0]:
			outputStr = char + outputStr;
		else:
			outputStr = outputStr + char;
		

	print("Case #%d: %s" %(i+1, outputStr) );
