#include <stdio.h>

int addNumbers(int n);

int main()
{
    int num;
    printf("Enter a positive integer: ");
    scanf("%d", &num);
    printf("Sum = %d\n",addNumbers(num));
    return 0;
}

int addNumbers (int n)
{
    int i, sum=0;
    for(i=1; i<=n; i++)
    {
    sum = sum + i;
    }
    return sum;
}