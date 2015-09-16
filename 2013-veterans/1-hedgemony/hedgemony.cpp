/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/2334486/dashboard#s=p0
 **************************************************************/

#include <iostream>

using namespace std;

void show(double hedge[], int N);

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
		//        show(hedge, N);
		for (int j = 1; j < N-1; j++) {
			double calculated = (hedge[j-1]+hedge[j+1])/2;
			if (hedge[j] > calculated) {
				hedge[j] = calculated;
			}
			//            show(hedge, N);           
		}
		cout << "Case #" << (i+1) << ": " << hedge[N-2] << endl;
	}
}

void show(double hedge[], int N) {
	cout << "[";
	for (int j = 0; j < N; j++) {
		cout << hedge[j] << " ";
	}
	cout << "]" <<endl;
}
