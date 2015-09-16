/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/32003/dashboard#s=p1
 **************************************************************/

#include "traverser.h"

void walk(traverser* ptr) {
	switch (ptr->curr) {
		case NORTH:	ptr->y--; if (ptr->y < ptr->min_y) ptr->min_y = ptr->y; break;
		case EAST:	ptr->x++; if (ptr->x > ptr->max_x) ptr->max_x = ptr->x; break;
		case SOUTH:	ptr->y++; if (ptr->y > ptr->max_y) ptr->max_y = ptr->y; break;
		case WEST:	ptr->x--; if (ptr->x < ptr->min_x) ptr->min_x = ptr->x; break;
	}
}

void left(traverser* ptr) {
	ptr->curr +=4;
	ptr->curr--;
	ptr->curr %= 4;
}

void right(traverser* ptr) {
	ptr->curr++;
	ptr->curr %= 4;
}

