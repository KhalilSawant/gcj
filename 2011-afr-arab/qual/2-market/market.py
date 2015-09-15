import sys;

f_ip = open(sys.argv[1],'r');
N = int(f_ip.readline());

for case in range(N):
	purse = int(f_ip.readline());
	price = map(int, f_ip.readline().split());
	
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
