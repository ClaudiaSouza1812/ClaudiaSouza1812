#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("what's x? ");
    int y = get_int("what's y? ");

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf("x is greater than y\n");
    }
    else
    {
        printf("x is iqual to y\n");
    }
}