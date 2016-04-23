/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/32003/dashboard#s=p1
 **************************************************************/

#include <stdio.h>
#include <string.h>
#include <malloc.h>

#include "traverser.h"

#define RUN_LENGTH (10000)

void find_R_C(const char* forward, const char* reverse, int forward_len, int reverse_len, int* R, int* C, int* init_x);
void paint(const char* forward, const char* reverse, int forward_len, int reverse_len, char** matrix, int R, int C, int init_x);
void print_matrix(char** matrix, int R, int C);

int main() {

	int N;
	scanf("%d", &N);

	int i;
	for (i = 0; i < N; i++) {
		char forward[RUN_LENGTH+1];
		scanf("%s", forward);
		int forward_len = strlen(forward);
		forward[forward_len] = 0;

		char reverse[RUN_LENGTH+1];
		scanf("%s", reverse);
		int reverse_len = strlen(reverse);
		reverse[reverse_len] = 0;

		int R, C, init_x;
		find_R_C(forward, reverse, forward_len, reverse_len, &R, &C, &init_x);

		char** matrix;
		matrix = (char**)malloc(R * sizeof(char*));
		int j;
		for (j = 0; j < R; j++) {
			matrix[j] = (char*)malloc(C * sizeof(char));
			int k;
			for (k = 0; k < C; k++) {
				matrix[j][k] = 0xf;
			}
		}

		paint(forward, reverse, forward_len, reverse_len, matrix, R, C, init_x);

		printf("Case #%d:\n", i+1);
		print_matrix(matrix, R, C);
	}

	return 0;
}

void find_R_C(const char* forward, const char* reverse, int forward_len, int reverse_len, int* R, int* C, int* init_x) {

	traverser me;
	me.x = 0;
	me.y = 0;
	me.curr = SOUTH;

	me.min_x = 0;
	me.max_x = 0;
	me.min_y = 0;
	me.max_y = 0;

	int i;
	for (i = 1; i < forward_len-1; i++) {
		switch(forward[i]) {
			case 'W':	walk(&me); break;
			case 'L':	left(&me); break;
			case 'R':	right(&me); break;
		}
	}	

	right(&me);
	right(&me);

	for (i = 1; i < reverse_len-1; i++) {
		switch(reverse[i]) {
			case 'W':	walk(&me); break;
			case 'L':	left(&me); break;
			case 'R':	right(&me); break;
		}
	}

	*C = me.max_x - me.min_x + 1;
	*R = me.max_y - me.min_y + 1;
	*init_x = -me.min_x;
}

void paint(const char* forward, const char* reverse, int forward_len, int reverse_len, char** matrix, int R, int C, int init_x) {

	traverser me;
	me.x = init_x;
	me.y = 0;
	me.curr = SOUTH;

	int i;
	for (i = 1; i < forward_len; i++) {
		switch(forward[i]) {
			case 'W':
				if (forward[i-1] != 'L') {
					switch (me.curr) {
						case NORTH:	matrix[me.y][me.x] &= ~(1 << WEST_WALL); break;
						case EAST:	matrix[me.y][me.x] &= ~(1 << NORTH_WALL); break;
						case SOUTH:	matrix[me.y][me.x] &= ~(1 << EAST_WALL); break;
						case WEST:	matrix[me.y][me.x] &= ~(1 << SOUTH_WALL); break;
					}
				}
				walk(&me);
				break;
			case 'L':	left(&me); break;
			case 'R':
				if (forward[i-1] != 'L') {
					switch (me.curr) {
						case NORTH:	matrix[me.y][me.x] &= ~(1 << WEST_WALL); break;
						case EAST:	matrix[me.y][me.x] &= ~(1 << NORTH_WALL); break;
						case SOUTH:	matrix[me.y][me.x] &= ~(1 << EAST_WALL); break;
						case WEST:	matrix[me.y][me.x] &= ~(1 << SOUTH_WALL); break;
					}
				}
				right(&me);
				break;
		}
	}

	right(&me);
	right(&me);
	walk(&me);

	for (i = 1; i < reverse_len; i++) {
		switch(reverse[i]) {
			case 'W':
				if (reverse[i-1] != 'L') {
					switch (me.curr) {
						case NORTH:	matrix[me.y][me.x] &= ~(1 << WEST_WALL); break;
						case EAST:	matrix[me.y][me.x] &= ~(1 << NORTH_WALL); break;
						case SOUTH:	matrix[me.y][me.x] &= ~(1 << EAST_WALL); break;
						case WEST:	matrix[me.y][me.x] &= ~(1 << SOUTH_WALL); break;
					}
				}
				walk(&me);
				break;
			case 'L':	left(&me); break;
			case 'R':
				if (reverse[i-1] != 'L') {
					switch (me.curr) {
						case NORTH:	matrix[me.y][me.x] &= ~(1 << WEST_WALL); break;
						case EAST:	matrix[me.y][me.x] &= ~(1 << NORTH_WALL); break;
						case SOUTH:	matrix[me.y][me.x] &= ~(1 << EAST_WALL); break;
						case WEST:	matrix[me.y][me.x] &= ~(1 << SOUTH_WALL); break;
					}
				}
				right(&me);
				break;
		}
	}
}

void print_matrix(char** matrix, int R, int C) {

	int i;
	for (i = 0; i < R; i++) {
		int j;
		for (j = 0; j < C; j++)
			printf("%x", matrix[i][j]);
		printf("\n");
	}
}
