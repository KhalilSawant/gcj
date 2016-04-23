#!/usr/bin/python
################################################################
#	Author:	Khalil Sawant
# https://code.google.com/codejam/contest/837485/dashboard#s=p1
################################################################

import sys;

N = int(raw_input());

for case in range(N):
	purse = int(raw_input());
	price = map(int, raw_input().split());
	
	bestBuy = -1;
	bestSell = -1;
	bestProfit = 0;
	
	for j in range(11):
		for k in range(j+1,12):
			if purse > price[j]:
				quantity = purse / price[j];
				investment = quantity * price[j];
				sellingPrice = quantity * price[k];
				profit = sellingPrice - investment;
				if profit > bestProfit:
					bestBuy = j;
					bestSell = k;
					bestProfit = profit;
				elif profit == bestProfit:
					if price[j] < price[bestBuy]:
						bestBuy = j;
						bestSell = k;
						bestProfit = profit;
	
	print "Case #" + str(case+1) + ":",
	if -1 == bestBuy:
		print "IMPOSSIBLE";
	else:
		print (bestBuy+1), (bestSell+1), bestProfit;
