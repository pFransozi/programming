#include<stdio.h>
#include<stdlib.h>
#define SIZE 21

int deQueueFront();
int deQueueRear();
void enQueueRear(int);
void enQueueFront(int);
void display();

int queue[SIZE];
int rear = 0, front = 0;

// main function definition
int main()
{
    char ch;
    int choice1, choice2, value;
    printf("Double Ended Queue: \n");

    do
    {
        printf("\n1.Input Restricted Double Ended Queue: \n");
        printf("2.Input Restricted Double Ended Queue: \n");
        printf("\nEnter your choice: ");
        scanf(" %d", &choice1);

        switch(choice1)
        {
            case 1:
                printf("\n Select the Operation: \n");
                printf("1.Insert from Front\n2.Delete from Rear\n3.Delete from Front\n4. Display");

                do
                {
                    printf("\nEnter your choice for the operation: ");
                    scanf(" %d",&choice2);
                    
                    switch(choice2)
                    {
                        case 1: 
                            enQueueRear(value);
                            display();
                            break;

                        case 2: 
                            value = deQueueRear();
                            printf("\nThe value deleted from rear end of Dequeue is %d",value);
                            display();
                            break;
                        
                        case 3: 
                            value=deQueueFront();
                            printf("\nThe value deleted from front end of Dequeue is %d",value);
                            display();
                            break;
                        case 4: 
                            display();
                            break;
                        
                        default:printf("Wrong choice");
                    }

                    printf("\nDo you want to continue another operation (Y/N): ");
                    scanf(" %c", &ch);
                
                }while(ch=='y'||ch=='Y');

                break;
            
            case 2 :
                printf("\nSelect the Operation:\n");
                printf("1. Insert at Rear\n2. Insert at Front\n3. Delete from Front\n4. Display");
                
                do
                {
                    printf("\nEnter your choice for the operation: ");
                    scanf(" %d",&choice2);
                    
                    switch(choice2)
                    {
                        case 1: 
                            enQueueRear(value);
                            display();
                            break;

                        case 2: 
                            enQueueFront(value);
                            display();
                            break;

                        case 3: 
                            value = deQueueFront();
                            printf("\nThe value deleted from front end of Dequeue is %d", value);
                            display();
                            break;

                        case 4: 
                            display();
                            break;

                        default: printf("Wrong choice");
                    }

                    printf("\nDo you want to continue another operation (Y/N): ");
                    scanf(" %c", &ch);
                } while(ch=='y'||ch=='Y');

                break;
        }
        printf("\nDo you want to continue (Y/N):");
        scanf(" %c", &ch);

    }while(ch=='y'||ch=='Y');

}

void enQueueRear(int data)
{
    char ch;
    if(front == SIZE/2)
    {
        printf("\nQueue is full");
        return;
    }

    do
    {
        printf("\nEnter the value to be insert:");
        scanf(" %d", &data);
        queue[front] = data;
        front++;
        printf("\nDo you want to continue insertion [y/n]");
        scanf(" %c", &ch);

    } while (ch == 'y');    
}

void enQueueFront(int data)
{
    char ch;
    if(front == SIZE/2)
    {
        printf("\nQueue is full.");
        return;
    }

    do
    {
        printf("\nEnter the value to be inserted:");
        scanf(" %d", &data);
        rear--;
        queue[rear] = data;
        printf("\nDo you wnat to continue insertion [y/n]");
        scanf(" %c", &ch);
    } while (ch == 'y');    
}

int deQueueRear()
{
    int deleted;
    if (front = rear)
    {
        printf("\nQueue is empty");
        return 0;
    }
    front--;
    deleted = queue[front+1];
    return deleted;
}

int deQueueFront()
{
    int deleted;
    if(front == rear)
    {
        printf("\nQueue is Empty.");
        return 0;
    }
    rear++;
    deleted = queue[rear-1];
    return deleted;
}

void display()
{
    int i;

    if (front == rear)
    {
        printf("\nQueue is Empty");

    }
    else
    {
        printf("\nThe Queue elements are:");
        for (i=rear; i < front; i++)
        {
            printf("%d\t", queue[i] );
        }
        
    }
}