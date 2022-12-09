#include <stdio.h>
#include <math.h>
#include <cs50.h>

/*
check50 says 378282246310005 and a couple others are VALID but

even: 38826105
odd : 7224300

even*2: 6+16+16+4+12+2+0+10

sum: 30 + 18 = 48

48 % 10 != 0

:( identifies 378282246310005 as AMEX
    expected "AMEX\n", not "INVALID\n"
*/

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

    string card;

    // print card type
    if (12 < length && length < 17 && narray[0] == 4) {
        card = "VISA\n";
    } else if (length == 15) {
        card = "AMEX\n";
    } else if (length == 16) {
        card = "MASTERCARD\n";
    } else {
        printf("INVALID\n");
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

    for (int i=0; i<half; i++) {
        even[i] *= 2;
    }


    int sum = 0;
    for (int i=0; i<half; i++) {
        sum += floor(even[i] / 10);
        sum += even[i] % 10;
        sum += odd[i];
    }

    if (sum % 10 == 0) {
        printf("%s", card);
    } else {
        printf("INVALID\n");
    }
}