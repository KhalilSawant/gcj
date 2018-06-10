#!/usr/bin/python
###########################################################################
#	Author:	Khalil Sawant
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard 
###########################################################################

import sys;

def calculate(sequence):
	power = 1;
	damage = 0;
	for i in sequence:
		if i == 'S':
			damage += power
		elif i == 'C':
			power *= 2;
		else:
			assert(0);
	return damage

T = int(raw_input());

for i in range(T):

	D, sequence = raw_input().split();
	D = int(D);

	swaps = 0;

	possible = (D >= calculate(sequence) );
	index = sequence.rfind('CS');

	while not possible and -1 != index:
		sequence = list(sequence);
		sequence[index] = 'S';
		sequence[index+1] = 'C';
		swaps += 1;
		sequence = "".join(sequence);

		if (D >= calculate(sequence) ):
			possible = True;
		index = sequence.rfind('CS');

	if possible:
		 print("Case #%d: %d" %(i+1, swaps) );
	else:
		print("Case #%d: IMPOSSIBLE" %(i+1) );

