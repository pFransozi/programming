#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 20

char str[MAX], stack[MAX];
int top = -1;

char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

void push(char c)
{
    stack[++top] = c;
}

char pop()
{
    return stack[top--];
}

void post_in()
{
    int n, i, j = 0;
    char a, b, op, x[20];

    printf("Enter the postfix expression: ");
    scanf(" %s", str);
    strrev(str);
    n = strlen(str);

    for (i = 0; i < MAX; i++)
        stack[i] = '\0';
    
    printf("Infix expression is: \t");
    for (i = 0; i < n; i++)
    {
        if (str[i] == '+' || str[i] == '-' || str[i] == '/' || str[i] == '*')
        {
            push(str[i]);
        }
        else
        {
            x[j] = str[i];
            j++;
            x[j] = pop();
            j++;
        }
    }

    x[j] = str[top--];
    strrev(x);
    printf("%s\n", x);
}

int main()
{
    int ch;
    while (1)
    {
        printf("Enter choice 1. Postfix to Infix; 2. Exit\n");
        scanf(" %d", &ch);

        switch (ch)
        {
        case 1:
            post_in();
            break;
        case 2:
            exit(0);
        
        default: printf("Wrong choice.\n");
        }

        printf("Enter 1 to continue, 0 to exit\n");
        scanf("%d", &ch);
        if (ch == 0)
        {
            break;
        }
    }
    return 0;
}