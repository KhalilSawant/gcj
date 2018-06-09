/*****************************************************************************
 *	Author:	Khalil Sawant						     *
 * https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard *
 *****************************************************************************/

#include <iostream>
#include <cassert>
#include <cmath>

using namespace std;

int main() {
	unsigned int T;
	cin >> T;
	for (unsigned int i = 0; i < T; i++) {
		cout << "Case #" << (i+1) << ": ";

		unsigned int C;
		cin >> C;

		unsigned int B[C];
		unsigned int totalBalls = 0;
		for (unsigned int j = 0; j < C; j++) {
			cin >> B[j];
			totalBalls += B[j];
		}
		assert(C == totalBalls);

		int ballToSlotMap[C];
		int shift[C];
		unsigned int ballNo = 0;
		for (int j = 0; j < C; j++) {
			for (unsigned int k = 0; k < B[j]; k++) {
				ballToSlotMap[ballNo] = j;
				shift[ballNo] = j-ballNo;
				ballNo++;
			}
		}

		if ( ballToSlotMap[0] == 0 && ballToSlotMap[C-1] == (C-1) ) {
			unsigned int largestDiff = 0;
			for (unsigned int j = 0; j < C; j++) {
				unsigned int diff = abs(shift[j]);
				if (diff > largestDiff) largestDiff = diff;
			}
			cout << largestDiff+1 << endl;
			char grid[largestDiff+1][C];
			for (unsigned int row = 0; row < largestDiff+1; row++) {
				for (unsigned int column = 0; column < C; column++) {
					grid[row][column] = '.';
				}
			}
			for (unsigned int j = 0; j < C; j++) {
				if (shift[j] < 0) {
					for (unsigned int k = 0; k < -shift[j]; k++) {
						grid[k][j-k] = '/';
					}
				} else {
					for (unsigned int k = 0; k < shift[j]; k++) {
						grid[k][j+k] = '\\';
					}
				}
			}
			
			for (unsigned int row = 0; row < largestDiff+1; row++) {
				for (unsigned int column = 0; column < C; column++) {
					cout << grid[row][column];
				}
				cout << endl;
			}
		} else cout << "IMPOSSIBLE" << endl;
	}
}

