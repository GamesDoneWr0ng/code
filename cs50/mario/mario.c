#include <stdio.h>

int main(void) 
{
    int height;

    // Asks for height until we get a valid input
    do {
        printf("Height: ");

        // get the input
        scanf("%d", &height);
    }
    while (height < 0 || height > 8);

    for (int row = 1; row <= height; row++) {

        // print height-row spaces 
        for (int n = 0; n < height-row; n++) {
            printf(" ");
        }

        // print row #
        for (int n = 0; n < row; n++) {
            printf("#");
        }

        // print two spaces
        printf("  ");

        // print row #
        for (int n = 0; n < row; n++) {
            printf("#");
        }

        // print height-row spaces
        for (int n = 0; n < height-row; n++) {
            printf(" ");
        }

        // next row
        printf("\n");
    }
}