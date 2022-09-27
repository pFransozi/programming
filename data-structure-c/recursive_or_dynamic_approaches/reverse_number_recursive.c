# include <stdio.h>

int reverse_function(int num);

int main()
{
    int num, reverse_number;

    printf("\nEnter any number.");
    scanf("%d", &num);

    reverse_number = reverse_function(num);
    printf("\nAfter reverse, the number is: %d\n", reverse_number);

    return 0;
}

int sum = 0, rem;
int reverse_function(int num)
{
    if (num)
    {
        rem = num % 10;
        sum = sum * 10 + rem;
        reverse_function(num/10);
    }
    else
        return sum;
}