/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/3264486/dashboard#s=p0
 **************************************************************/

#include <stdio.h>
#include <string.h>

int main() {

	unsigned int T;
	scanf("%d", &T);

	unsigned int i;
	for (i = 0; i < T; i++) {
		char S[1005];
		scanf("%s", S);

		int K;
		scanf("%d", &K);

		unsigned int len = strlen(S);

		unsigned int count = 0;

		unsigned int j;
		for (j = 0; j < len-(K-1); j++) {

			if ('+' == S[j]) continue;
 
			unsigned int k;
			for (k  = 0; k < K; k++) { // flip
				if ('-' == S[j+k]) S[j+k] = '+';
				else S[j+k] = '-';
			}
			count++;
		}

		unsigned int possible = 1;
		for (j = len-(K-1); j < len; j++) {
			if ('-' == S[j]) {
				possible = 0;
				break;
			}
		}

		if (possible) printf("Case #%u: %u\n", (i+1), count);
		else printf("Case #%u: %s\n", (i+1), "IMPOSSIBLE");
	}
	return 0;
}
