/*

This stack is implemented over an array. Therefore it is a limit, which is 5 in this example.

The push and pop function have a constant time complexity in the worst case, O(1); as well
space complexity.

The display function has a linear time complexity, because the algorithm runs the array through
each element in the array. The space complexity is constant.

*/


#include<stdio.h>
#include<stdlib.h>
#define max 5
int stack[max];
int top;

// function declaration
void push(int);
int pop();
void display();

int main()
{
    int choice;
    int data;
    char ch;
    top = -1;

    printf("Stack Implementation using array: \n");

    do
    {
        printf("1. Push\n2. Pop\n3. Display\n4. Exit\n");
        printf("\nEnter your choice: \n");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                push(data);
                break;
            case 2:
                data = pop();
                printf("Popped element = %d \n", data);
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("\n Wrong choice.\n");
        }

        fflush(stdin);
        printf("Do you want to continue [y/n] : ");
        scanf(" %c",&ch);
    } while (ch == 'y');

    return 0;    
}

void push(int a)
{
    if (top == max -1)
    {
        printf("\n stack is full\n");
        return;
    }
    else
    {
        top++;
        stack[top] = a;
    }
}

int pop()
{
    int item;
    if (top == -1)
    {
        printf("\n stack if empty\n");
    }
    else
    {
        item = stack[top];
        top--;
    }
    return (item);
}

void display()
{
    int i;
    if (top == -1)
    {
        printf("\n stack is empty\n");
    }
    else
    {
        printf("Elements in the stack are: ");
        for (i =top; i>= 0; i--)
        {
            printf("%d\t ", stack[i]);
        }

        printf("\n");
    }
}