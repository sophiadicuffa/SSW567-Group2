#include <stdio.h>
#include <string.h>

// Source: https://www.javatpoint.com/reverse-a-string-in-c
void example_function(char *input)
{
    // declare variable
    int i, len, temp;
    len = strlen(input); // use strlen() to get the length of str string

    // use for loop to iterate the string
    for (i = 0; i < len / 2; i++)
    {
        // temp variable use to temporary hold the string
        temp = input[i];
        input[i] = input[len - i - 1];
        input[len - i - 1] = temp;
    }
}

int main()
{
    char test[] = "Hello World";
    example_function(test);
    printf("%s", test);
}