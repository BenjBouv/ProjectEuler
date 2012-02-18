# include <stdio.h>
# include <stdlib.h>

#define NUMBER_OF_DIGITS 1000
#define FRAME 5

int main() {
	FILE* file = fopen("number.txt", "r");
	char number[NUMBER_OF_DIGITS];
	int i,j;
	int position = 0;
	int maxProduct = 0;

	if (file == NULL) {
		fprintf(stderr, "Error when getting the number.\n");
		exit(EXIT_FAILURE);
	}

	fgets(number, NUMBER_OF_DIGITS, file);
	fclose(file);

	for (i = 0; i < NUMBER_OF_DIGITS - FRAME; ++i)
	{
		char buffer[FRAME][2];
		int product = 1;

		for (j = 0; j < FRAME; ++j) {
			buffer[j][0] = number[position+j];
			buffer[j][1] = '\0';
		}
		for (j = 0; j < FRAME; ++j) {
			product *= atoi(buffer[j]);
		}

		if (product > maxProduct) {
			maxProduct = product;
		}

		position++;
	}

	printf("The solution to the 8th Project Euler's problem is %d.\n", maxProduct);

	return 0;
}
