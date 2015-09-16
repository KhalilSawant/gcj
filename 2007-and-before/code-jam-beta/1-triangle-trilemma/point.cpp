/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/32014/dashboard#s=p0
 **************************************************************/

#include "point.h"

bool Point::equals(const Point& other) {
	return ( (x == other.x) && (y == other.y) );
}

unsigned int Point::distanceSquared(const Point& other) {
	int diff_x = x - other.x;
	int diff_y = y - other.y;
	return (diff_x*diff_x + diff_y*diff_y);
}

double Point::slope(const Point& other) {
	int diff_x = x - other.x;
	int diff_y = y - other.y;
	return ( (double)diff_y ) / diff_x;
}
