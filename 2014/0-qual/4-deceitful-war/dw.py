#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/2974486/dashboard#s=p3
################################################################

import sys;

T = int(raw_input());

for i in range(T):
	N = int(raw_input());
	naomi = list(map(float,raw_input().split()))
	ken = list(map(float,raw_input().split()))
	
	naomi.sort()
	ken.sort()
	
	naomi_deceit = naomi[:]
	ken_deceit = ken[:]
	
	deceit_wins = 0;

	while len(naomi_deceit) > 0:
		if naomi_deceit[0] < ken_deceit[0]:
			ken_deceit.pop(-1)			
		else:
			ken_deceit.pop(0)
			deceit_wins = deceit_wins + 1;

		naomi_deceit.pop(0)

	while len(naomi) > 0:
		for j in range(len(ken)):
			if ken[j] > naomi[0]:
				ken.pop(j)
				break;		
		naomi.pop(0)
	print("Case #%d: %d %d" %(i+1, deceit_wins, len(ken)));
