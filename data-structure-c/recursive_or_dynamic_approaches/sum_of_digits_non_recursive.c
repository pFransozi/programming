#include<stdio.h>
int sum_of_digit(int n)
{
    int r,sum =0;
    
    do
    {
        r = n % 10; // separate first digit of a number
        sum = sum + r; // add the separated digit in the intermediate variable
        n = n/10; // delete first digit of a number
        
    } while (n > 0);

    return sum;
    
}

int main()
{
    int number;

    printf("Enter a number to sum its digits\n");
    scanf("%d", &number);

    int result = sum_of_digit(number);
    printf("Sum of digits in %d is %d\n", number, result);
    return 0;
}