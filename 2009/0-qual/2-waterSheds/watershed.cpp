/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/90101/dashboard#s=p1
 **************************************************************/

#include <iostream>

char get_basin(int** terrain, char** basin, int H, int W, int j, int k);
char global_basin_char = 0;

int main() {

	unsigned int T;
	std::cin >> T;

	int i;
	for (i = 0; i < T; i++) {

		global_basin_char = 'a';
		
		unsigned int H;
		std::cin >> H;
		unsigned int W;
		std::cin >> W;

		int** terrain;
		terrain = new int*[H];
		char** basin;
		basin = new char*[H];

		unsigned int j;
		for (j = 0; j < H; j++) {
			terrain[j] = new int[W];
			basin[j] = new char[W];
		}

		for (j = 0; j < H; j++) {
			unsigned int k;
			for (k = 0; k < W; k++) {
				std::cin >> terrain[j][k];
				basin[j][k] = '*';
			}
		}

		for (j = 0; j < H; j++) {
			unsigned int k;
			for (k = 0; k < W; k++) {
				basin[j][k] = get_basin(terrain, basin, H, W, j, k);
			}
		}

		std::cout << "Case #" << i+1 << ":" << std::endl;
		for (j = 0; j < H; j++) {
			unsigned int k;
			for (k = 0; k < W; k++) {
				std::cout << basin[j][k] << " ";
			}
			std::cout << std::endl;
		}

	}
}

char get_basin(int** terrain, char** basin, int H, int W, int j, int k) {
	if ('*' == basin[j][k]) {
		int fall = 0;
		unsigned int down_neighbor_j;
		unsigned int down_neighbor_k;
	
		if (j > 0 && (terrain[j][k] - terrain[j-1][k]) > fall) {	// North
			fall = terrain[j][k] - terrain[j-1][k];
			down_neighbor_j = j-1;
			down_neighbor_k = k;
		}
		if (k > 0 && (terrain[j][k] - terrain[j][k-1]) > fall) {	// West
			fall = terrain[j][k] - terrain[j][k-1];
			down_neighbor_j = j;
			down_neighbor_k = k-1;
		}
		if (k < W-1 && (terrain[j][k] - terrain[j][k+1]) > fall) {	// East
			fall = terrain[j][k] - terrain[j][k+1];
			down_neighbor_j = j;
			down_neighbor_k = k+1;
		}
		if (j < H-1 && (terrain[j][k] - terrain[j+1][k]) > fall) {	// South
			fall = terrain[j][k] - terrain[j+1][k];
			down_neighbor_j = j+1;
			down_neighbor_k = k;
		}
		if (0 == fall) {	// I am sink
			basin[j][k] = global_basin_char++;
		} else {
			basin[j][k] = get_basin(terrain, basin, H, W, down_neighbor_j, down_neighbor_k);
		}		
	}
	return basin[j][k];
}
