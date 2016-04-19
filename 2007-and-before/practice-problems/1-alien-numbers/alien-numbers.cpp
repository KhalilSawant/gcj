/***************************************************************
 *	Author:	Khalil Sawant
 * https://code.google.com/codejam/contest/32003/dashboard#s=p0
 **************************************************************/

#include <iostream>
#include <string.h>
#include <math.h>

#define MAX_DIGITS_IN_LANGUAGE (94)
#define MAX_DIGITS_IN_NUMBER (32)
#define ASCII_DIGITS (256)

int main() {

	unsigned int N;
	std::cin >> N;

	for (unsigned int i = 0; i < N; i++) {

		char alien_number[MAX_DIGITS_IN_NUMBER];
		char source_language[MAX_DIGITS_IN_LANGUAGE+1];
		char target_language[MAX_DIGITS_IN_LANGUAGE+1];

		std::cin >> alien_number;
		std::cin >> source_language;
		std::cin >> target_language;

		char source_hash[ASCII_DIGITS];
		char target_hash[ASCII_DIGITS];

		unsigned int source_language_size = strlen(source_language);
		for (unsigned int j = 0; j < source_language_size; j++) {
			source_hash[(unsigned int)source_language[j]] = j;
		}
		unsigned int target_language_size = strlen(target_language);
		for (unsigned int j = 0; j < target_language_size; j++) {
			target_hash[(unsigned int)target_language[j]] = j;
		}

		unsigned int alien_number_size = strlen(alien_number);
		unsigned long long result_in_decimal = 0;
		for (int j = alien_number_size-1, k = 0; j >=0; j--, k++) {
			result_in_decimal += source_hash[ (unsigned int)alien_number[j] ] * pow(source_language_size,k);
		}

		char alien_number_in_target_and_reversed[MAX_DIGITS_IN_NUMBER];
		unsigned int no_of_digits_in_alien_number_in_target = 0;
		while (result_in_decimal != 0) {
			alien_number_in_target_and_reversed[no_of_digits_in_alien_number_in_target++] = target_language[result_in_decimal%target_language_size];
			result_in_decimal /= target_language_size;
		};
		alien_number_in_target_and_reversed[no_of_digits_in_alien_number_in_target] = 0;

		std::cout << "Case #" << (i+1) << ": ";
		for ( int j = no_of_digits_in_alien_number_in_target-1; j >= 0 ; j--) {
			std::cout << alien_number_in_target_and_reversed[j];
		}
		std::cout << std::endl;
	}
}
