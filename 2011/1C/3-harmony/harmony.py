import sys;
import fractions;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

def lcm(a,b):
	if a == 0 or b == 0:
		return 0;
	else:
		return (a*b)/fractions.gcd(a,b);

for case in range(T):
	N,L,H = map(int, f_ip.readline().split());
	frequencies = map(int, f_ip.readline().split());
	impossible = True;
	frequencies.sort();

	GCD = reduce(fractions.gcd, frequencies)
	LCM = reduce(lcm,frequencies);
	
	if L < GCD:
		for possible in range(L,GCD):
			if GCD % possible == 0:
				result = possible;
				impossible = False;
	else:
		for iter in range(len(frequencies)-1):
			first_half_lcm = reduce(lcm, frequencies[:iter+1]);
			second_half_gcd = reduce(fractions.gcd, frequencies[iter+1:]);
			if first_half_lcm <= second_half_gcd:
				for possible in range(first_half_lcm, second_half_gcd+1):
					if possible >= L and possible <= H:
						if possible % first_half_lcm == 0 and second_half_gcd % possible == 0:
							impossible = False;
							result = possible;
							break;
			if not impossible:
				break;
		
		if impossible and frequencies[-1] <= H:
			if H >= LCM:
				impossible = False;
				result = LCM;

	print "Case #" + str(case+1) + ":",
	if impossible:
		print "NO";
	else:
		print result;
