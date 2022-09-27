/*

This algorithm uses an array to implements a queue, and uses two indexes to move in this array
defining the front of the queue and the rear. On the one hand, the insertion is deletion have
O(1) time complexity, but the use of array is not so clever because the algorithm does not
relocate the array.

The empty, full, insert and delete methods are O(1);
Display function is O(n);

*/

#include <stdio.h>
#include <stdlib.h>
#define MAX 5

struct queue
{
    int que[MAX];
    int front, rear;
} q;

int empty()
{
    if (q.front == -1 || q.front>q.rear)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int full()
{
    if (q.rear >= MAX -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void insert(int data)
{
    if (q.front == -1)
    {
        q.front++;
    }
    q.que[++q.rear] = data;
}

void delete()
{
    int data;
    data = q.que[q.front];
    q.front++;
    printf("Deleted element = %d\n", data);
}

void display()
{
    int i;
    i=q.front;

    printf("Queue elements are: ");
    for(;i<=q.rear;i++)
    {
        printf("\t%d", q.que[i]);
    }
    printf("\n");
}

int main()
{
    int choice, data;
    char ch;

    q.front = -1;
    q.rear = -1;

    do
    {
        printf("Linear queue implementation using array: ");
        printf("\n1.Insert\n2.Delete\n3.Display\n4.Exit");
        printf("\nEnter choice: ");
        scanf(" %d", &choice);

        switch (choice)
        {
        case 1:

            if(full())
            {
                printf("\n Queue is full");
            }
            else
            {
                printf(" Enter data: ");
                scanf(" %d",&data);
                insert(data);
            }
            break;

        case 2:

            if(empty())
                printf("\n Queue is empty");
            else
                delete();
            break;

        case 3:

            if(empty())
                printf("\n Queue is empty");
            else
                display();
            break;

        case 4: exit(0);
        
        default: printf("\nWrong choice!");
        }

        printf("\nDo you want to continue ... [y/n]");
        fflush(stdin);
        scanf(" %c", &ch);

    } while (ch == 'y');

    return 0;    
}
