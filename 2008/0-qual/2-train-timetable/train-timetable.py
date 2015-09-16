################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/32013/dashboard#s=p1
################################################################

import sys
from collections import deque;

f_ip = open(sys.argv[1], 'r');
N = int(f_ip.readline());

for i in range(N):
	turn = int(f_ip.readline());
	no_of_trips = f_ip.readline().split();
	NA = int(no_of_trips[0]);
	NB = int(no_of_trips[1]);

	trips_a = [];
	trips_b = [];

	for j in range(NA):
		trip = f_ip.readline().split();
		departure = trip[0];
		arrival = trip[1];

		hrs = int(departure.split(':')[0]);
		mins = int(departure.split(':')[1]);
		trips_a.append( (60*hrs+mins,1) );

		hrs = int(arrival.split(':')[0]);
		mins = int(arrival.split(':')[1]);
		trips_b.append( (60*hrs+mins+turn,-1) );

	for j in range(NB):
		trip = f_ip.readline().split();
		departure = trip[0];
		arrival = trip[1];

		hrs = int(departure.split(':')[0]);
		mins = int(departure.split(':')[1]);
		trips_b.append( (60*hrs+mins,1) );

		hrs = int(arrival.split(':')[0]);
		mins = int(arrival.split(':')[1]);
		trips_a.append( (60*hrs+mins+turn,-1) );
		
	trips_a.sort();
	trips_b.sort();

	while trips_a:
		last = trips_a.pop();
		if last[1] == 1:
			trips_a.append(last);
			break;
	while trips_b:
		last = trips_b.pop();
		if last[1] == 1:
			trips_b.append(last);
			break;

	stored_for_a = 0;
	needed_for_a = 0;
	for j in trips_a:
		if j[1] == 1:
			if stored_for_a > 0:
				stored_for_a -= 1;
			else:
				needed_for_a += 1;
		else:
			stored_for_a += 1;

	stored_for_b = 0;
	needed_for_b = 0;
	for j in trips_b:
		if j[1] == 1:
			if stored_for_b > 0:
				stored_for_b -= 1;
			else:
				needed_for_b += 1;
		else:
			stored_for_b += 1;

	print "Case #" + str(i+1) + ":",
	print needed_for_a, needed_for_b;
