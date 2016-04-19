/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/6254486/dashboard#s=p1
 **************************************************************/

#include <stdio.h>
#include <string.h>

int main() {

	unsigned int T;
	scanf("%d", &T);

	unsigned int i;
	for (i = 0; i < T; i++) {
		char S[105];
		scanf("%s", S);

		unsigned int len = strlen(S);
		S[len] = '+';

		int ptr = len;
		unsigned int count = 0;

		while (ptr > 0) {
			if (S[ptr] != S[ptr-1]) count++;
			ptr--;
		}

		printf("Case #%u: %u\n", (i+1), count);
	}
}
