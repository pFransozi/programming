# include <stdio.h>

int isPrime(int, int);

int main()
{
    int num, prime;
    printf("Enter a positive number: ");

    scanf("%d", &num);
    prime = isPrime(num, num / 2);

    if (prime == 1)
        printf("%d is a prime number\n", num);
    else
        printf("%d is not a prime number\n", num);

    return 0;
}

int isPrime(int num, int n)
{
    int i;
    for(i = n; i >= 2; i--)
    {
        if(num % i == 0)
            return 0;
    }
    return 1;
}