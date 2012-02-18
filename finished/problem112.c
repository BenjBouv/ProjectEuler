# include <stdio.h>

short isBouncy(int number) {
	short isIncreasing = 1, isDecreasing = 1;
	short digit, lastDigit = -1;
	while (number >= 10) {
		digit = number % 10;
		if (lastDigit != -1) {
			if (lastDigit > digit) {
				isDecreasing = 0;
				if (!isIncreasing)
					return 1;
			} else if (lastDigit < digit) {
				isIncreasing = 0;
				if (!isDecreasing)
					return 1;
			}
		}
		number = number / 10;
		lastDigit = digit;
	}

	if (lastDigit != -1) {
		if (lastDigit > number) {
			isDecreasing = 0;
		} else if (lastDigit < number) {
			isIncreasing = 0;
		}
	}

	return (!isDecreasing && !isIncreasing);
}

int main(void) {
	int n = 99; /* one before first number tested */
	int p = 99; /* proportion asked */

	int numberOfBouncies = 0;
	while (numberOfBouncies * 100 != p * n) {
		n++;
		if (isBouncy(n)) {
			numberOfBouncies++;
		}
	}

	printf("Number of bouncy numbers before %d is %d.\n", n, numberOfBouncies);
	return 0;
}
