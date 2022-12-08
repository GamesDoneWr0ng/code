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
    while (number < 1);

    //length of the number
    int length = floor(log10(number)) + 1;

    // the number as an array
    int narray[length];

    for (int i=length-1; i>=0; i--) {
        narray[i] = number % 10;
        number = floor(number / 10);
    }

    // print card type
    if (12 < length && length < 17 && narray[length-1] == 4) {
        printf("Visa\n");
    } else if (length == 15) {
        printf("American Express\n");
    } else if (length == 16) {
        printf("MasterCard\n");
    } else {
        printf("Invalid card\n");
        return 0;
    }
    
    int half = floor(length/2);

    int odd[half];

    // adds one to half if length is odd
    if (length % 2 != 0) {
        half++;
    }
    
    int even[half];

    // split the number as an array into two smaller odd and even arrays
    for (int i=0; i<length; i++) {
        if (i % 2 == 0) {
            even[i / 2] = narray[i];
        } else {
            odd[(i-1) / 2] = narray[i];
        }
    }

    for (int i=0; i<sizeof(even) / sizeof(even[0]); i++) {
        even[i] *= 2;
    }


    int sum;
    for (int i=0; i<half; i++) {
        sum += floor(even[i] / 10);
        sum += even[i] % 10;
        sum += odd[i];
    }

    if (sum % 10 == 0) {
        printf("Valid card!\n");
    } else {
        printf("Invalid card!\n");
    }
}