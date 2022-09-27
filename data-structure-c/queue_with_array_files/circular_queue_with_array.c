#include<stdio.h>
#include<stdlib.h>
#define MAX 5

int que[MAX];
int front, rear;

int full()
{
    if (front == (rear + 1) % MAX)
        return 1;
    else
        return 0;
}

int empty()
{
    if (front == -1)
        return 1;
    else
        return 0;
}

void insert(int data)
{
    if(front == -1)
    {
        front = rear = 0;
        que[rear] = data;
    }
    else
    {
        rear = (rear + 1)%MAX;
        que[rear] = data;
    }
}

void delete()
{
    int data;
    if (front == rear)
    {
        data = que[front];
    }
    else
    {
        data = que[front];
        front=(front+1)%MAX;
    }

    printf("Deleted element = %d\n", data);
}

void display()
{
    int i = front;
    printf("Elements in circular queue are: ");

    do
    {
        printf("\t%d", que[i]);
        i=(i+1)%MAX;
    } while (i != ((rear+1)%MAX));

    printf("\n");
    
}

int main()
{
    int choice, data;
    char ch;
    front = -1;
    rear = -1;

    do
    {
        printf("Circular Queue: ");
        printf("\n1:Insert\n2:Delete\n3:display\n4.Exit\n");
        printf("Enter your choice:");
        scanf(" %d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter data: ");
            scanf(" %d", &data);
            if(full())
                printf("\nQueue is full.");
            else
                insert(data);
            break;
        case 2:
            if (empty())
                printf("\bCircular queue is empty.");
            else
                delete();
            break;
        case 3:
            if (empty())
                printf("\nCircular queue is empty");
            else
                display();
            break;
        case 4: exit(0);

        
        default: printf("Wrong choice!"); break;
        }

        printf("\nDo you want to continue ... [y/n]: ");
        fflush(stdin);
        scanf(" %c", &ch);
    } while (ch=='y');

    return 0;    
}