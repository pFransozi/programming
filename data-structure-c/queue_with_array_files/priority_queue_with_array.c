#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int que[MAX];
int front, rear;

int empty()
{
    if (front == -1 || front > rear)
        return 1;
    else
        return 0;
}

int full()
{
    if (rear >= MAX - 1)
        return 1;
    else
        return 0;
}

void priority();

void insert(int data)
{
    if (front == -1)
        front++;
    
    que[++rear] = data;
    priority();
}

void priority()
{
    int i, j, temp;

    for (i = front; i < rear; i++)
    {
        for(j=front; j<rear; j++)
        {
            if (que[j] > que[j+1])
            {
                temp = que[j];
                que[j] = que[j+1];
                que[j+1] = temp;
            }
        }
    }
}

void delete()
{
    int data;
    data = que[front];
    front++;
    printf("\nDeleted element = %d \n", data);
}

void display()
{
    int i;
    i = front;
    printf("Elements in priority queue: ");
    while (i<=rear)
    {
        printf("\t%d", que[i]);
        i++;
    }
}

int main()
{
    int choice, data;
    char ch;
    front=-1;
    rear=-1;

    do
    {
        printf(" Priority Queue");
        printf(" 1:insert\t2:delete\t3:display\t4:exit");
        printf("\n Enter your choice");
        scanf(" %d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter data: ");
                scanf("%d",&data);
                if(full())
                    printf("\n Queue is full");
                else
                    insert(data);
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
            default: printf("\n Wrong choice");
        }
        
        printf(" Do you want to continue[y/n]");
        fflush(stdin);
        scanf(" %c",&ch);
    }while(ch=='y');
return 0;
}