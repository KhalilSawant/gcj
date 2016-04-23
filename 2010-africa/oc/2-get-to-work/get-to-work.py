#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/438101/dashboard#s=p1
################################################################

import sys

f_ip = open(sys.argv[1], 'r');
C = int(f_ip.readline());

for i in range(C):

	N,T = f_ip.readline().split();
	N = int(N);	T = int(T);
	E = int(f_ip.readline());

	towns = [];			# One list per town, list of capacties per car

	for j in range(N):
		towns.append([]);

	for j in range(E):
		H,P = f_ip.readline().split();
		H = int(H);	P = int(P);
		town_data = towns[H-1];
		town_data.append(P);
	
	for j in range(N):
		town_data = towns[j];
		town_data.sort();

	possible = True;
	result = [];

	for j in range(N):
		no_of_cars = 0;
		if j != T-1:	# Town not same as office
			town_data = towns[j];
			head_count = len(town_data);
			cars_capacity = sum(town_data);
			
			if head_count <= cars_capacity:	# Solution Possible
				while head_count > 0:
					lot = town_data.pop();
					no_of_cars += 1;
					head_count -= lot;						
				result.append(no_of_cars);
			else:
				possible = False;
				break;
		else:
			result.append(no_of_cars);

	if possible:
		print "Case #" + str(i+1) + ":",
		for j in range(N):
			print result[j],;
		print "";
	else:
		print "Case #" + str(i+1) + ": IMPOSSIBLE";
