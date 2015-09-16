/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/1460488/dashboard#s=p1
 **************************************************************/

#include <iostream>

int main() {

	unsigned int T;
	std::cin >> T;
	
	unsigned int i;
	for (i = 0; i < T; i++) {
		unsigned int N;
		std::cin >> N;
		unsigned int S;
		std::cin >> S;
		unsigned int p;
		std::cin >> p;

		unsigned int calculated_S = 0;
		unsigned int greater_than_p = 0;

		for (unsigned int j = 0; j < N; j++) {
			unsigned int data;
			std::cin >> data;

			if (data > 28) {
				// (10,10,10) or (10,10,9)
				greater_than_p++;
			} else if (data < 2) {
				// (0,0,0) or (0,0,1)
				if (p <= data)	greater_than_p++;
			} else {
				switch(data%3) {
					case 0:
						// (x,x,x) or (x, x+1, x+2)
						// If I get 12, express it as (4,4,4) or (3,4,5)
						// Second is S, but gives better max
						if (
							( (data/3) < p ) 
							&&
							( ( (data/3)+1) >= p)
						) {
							if (calculated_S < S) {
								calculated_S++;
								greater_than_p++;
							}
						} else if ( (data/3) >= p ) {
							greater_than_p++;
						}
						break;
					case 1: 
						// (x,x,x+1) or (x, x+2, x+2)
						// If I get 13, express it as (4,4,5) rather than (3,5,5)
						// to avoid wasting S, because max in both case is 5
						if ( ((data/3)+1) >= p ) {
							greater_than_p++;
						}
						break;
					case 2:
						// (x,x,x+2) or (x, x+1, x+1)
						// If I get 14, express it as (4,4,6) or (4,5,5)
						// First is S, but gives better max
						if (
							( ( (data/3)+1) < p )
							&&
							( ( (data/3)+2) >= p )
						) {
							if (calculated_S < S) {
								calculated_S++;
								greater_than_p++;
							}
						} else if ( ((data/3)+1) >= p ) {
							greater_than_p++;
						}
						break;
				}
			}
		}
		std::cout << "Case #" << (i+1) << ": "<< greater_than_p << std::endl;
	}
}
