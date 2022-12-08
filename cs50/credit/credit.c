#include <stdio.h>
#include <math.h>

int main(void) 
{
    long number;

    do {
        printf("Number: ");

        // ask for number
        scanf("%lu", &number);
    }
    while (number > 0);

    //length of the number
    int length = floor(log10(number)) + 1;

    // the number as an array
    int narray[length];

    for (int i=length-1; i>0; i--) {
        narray[i] = number % 10;
        number = floor(number / 10);
    }

    // print card type
    if (12 < length < 17 && narray[0] == 4) {
        printf("\nVisa\n");
    } else if (length == 15) {
        printf("\nAmerican Express\n");
    } else if (length == 16) {
        printf("\nMasterCard\n");
    } else {
        printf("\nInvalid card\n");
        return 0;
    }

    int even[length];
    int odd[length];

    for (int i=0; i<length; i++) {
        if (i % 2 == 0) {
            even[i / 2] = narray[i];
        } else {
            even[(i-1) / 2] = narray[i];
        }
    }
}