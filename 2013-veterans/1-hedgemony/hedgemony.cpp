/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/2334486/dashboard#s=p0
 **************************************************************/

#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;

		double hedge[N];
		for (int j = 0; j < N; j++) {
			cin >> hedge[j];
		}

		for (int j = 1; j < N-1; j++) {
			double calculated = (hedge[j-1]+hedge[j+1])/2;
			if (hedge[j] > calculated) {
				hedge[j] = calculated;
			}
		}
		cout << "Case #" << (i+1) << ": " << hedge[N-2] << endl;
	}
}
