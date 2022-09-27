#include <stdio.h>

int reverse_function(int num);

int main()
{
    int num, reverse_number;
    printf("\nEnter any number ");
    scanf("%d", &num);

    reverse_number = reverse_function(num);
    printf("\nAfter reverse, the number is: %d\n", reverse_number);

    return 0;
}

int rev=0, rem;
int reverse_function(int num)
{
    while (num != 0)
    {
        rem = num % 10;
        rev = (rev * 10) + rem;
        num = num / 10;
    }

    return rev;
    
}