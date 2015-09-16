/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/32014/dashboard#s=p0
 **************************************************************/

#include <iostream>

#include "point.h"

#define NO_OF_POINTS (3)

void sort(unsigned long long int* const distance);

int main() {

	unsigned int N;
	std::cin >> N;

	for (unsigned int i = 0; i < N; i++) {
		Point p[NO_OF_POINTS];

		for (int j = 0; j < NO_OF_POINTS; j++) {
			int x,y;
			std::cin >> x;	p[j].setX(x);
			std::cin >> y;	p[j].setY(y);			
		}

		unsigned long long int distSquared[NO_OF_POINTS];
		for (int j = 0; j < NO_OF_POINTS; j++) {
			distSquared[j] = p[j].distanceSquared(p[(j+1)%NO_OF_POINTS]);
		}

		if ( 0 == distSquared[0] || 0 == distSquared[1] || 0 == distSquared[2] )  {
			std::cout << "Case #" << (i+1) << ": not a triangle" << std::endl;
		} else {
			sort(distSquared);
			if ( distSquared[2] < (distSquared[1]+distSquared[0]) ) {	// Acute				
				if (
					(distSquared[2] == distSquared[1]) || 		// Less than 60 deg
					(distSquared[1] == distSquared[0])		// More than 60 deg
				) {
					std::cout << "Case #" << (i+1) << ": isosceles acute triangle" << std::endl;
				} else {
					std::cout << "Case #" << (i+1) << ": scalene acute triangle" << std::endl;
				}
			} else if ( distSquared[2] == (distSquared[1]+distSquared[0]) ) {	// Right
				if (distSquared[1] == distSquared[0]) {
					std::cout << "Case #" << (i+1) << ": isosceles right triangle" << std::endl;
				} else {
					std::cout << "Case #" << (i+1) << ": scalene right triangle" << std::endl;
				}
			} else {							// Obtuse
				if (distSquared[1] == distSquared[0]) {
					if (distSquared[2] == 4*distSquared[1] ) {
						std::cout << "Case #" << (i+1) << ": not a triangle" << std::endl;
					} else {
						std::cout << "Case #" << (i+1) << ": isosceles obtuse triangle" << std::endl;
					}
				} else {
					unsigned long long int two_ab = distSquared[2] - (distSquared[1]+distSquared[0]);
					if ( (two_ab*two_ab) == (4*distSquared[1]*distSquared[0]) ) {
						std::cout << "Case #" << (i+1) << ": not a triangle" << std::endl;
					} else {
						std::cout << "Case #" << (i+1) << ": scalene obtuse triangle" << std::endl;
					}
				}
			}
		}

	}
}

void sort(unsigned long long int* const distSquared) {
	unsigned long long temp;
	if (distSquared[0] > distSquared[1]) {
		temp = distSquared[0];
		distSquared[0] = distSquared[1];
		distSquared[1] = temp;
	}
	if (distSquared[1] > distSquared[2]) {
		temp = distSquared[1];
		distSquared[1] = distSquared[2];
		distSquared[2] = temp;
	}
	if (distSquared[0] > distSquared[1]) {
		temp = distSquared[0];
		distSquared[0] = distSquared[1];
		distSquared[1] = temp;
	}
}

