#include<stdio.h>

/*
I this error when i try to use get_string():

Undefined symbols for architecture arm64:
  "_get_string", referenced from:
      _main in hello-f8ca65.o
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [hello] Error 1

-v gave me:
GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
*/

int main()
{
    char name[10];

    printf("What is your name? ");
    
    //get string input.
    scanf("%s",name);
    
    //print the name
    printf("Hello %s\n",name);
}