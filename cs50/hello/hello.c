#include<stdio.h>

int main()
{
    char name[10];

    printf("What is your name? ");
    
    //get string input.
    scanf("%s",name);
    
    //print the name
    printf("Hello %s\n",name);
}