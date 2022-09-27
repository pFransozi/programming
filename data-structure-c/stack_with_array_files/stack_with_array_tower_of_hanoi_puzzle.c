/*
Time complexity is calculated from the two recursions with base condition n == 1.
So n will go until n == 1, decrementing 1 in each recursion.

The math is (source https://quescol.com/data-structure/time-complexity-of-tower-of-hanoi):

T(n-1) is the time required to move n-1 disks from source to aux;
Moving nth disk from source to dest requires 1 step.
T(n-1) is the time required to move n-1 disks aux source to dest;

T(n) == T(n-1) + 1 + T(n-1)
T(n) == 2T(n - 1) + 1

.
.
.

T(n) == O(2^n)

*/

#include <stdio.h>

void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod)
{
    if (n == 1)
    {
        printf("\n Move disk 1 from rod %c to rod %c.", from_rod, to_rod);
        return;
    }

    towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
    printf("\n Move disk %d from rod %c to rod %c.", n, from_rod, to_rod);
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod);
}

int main()
{
    int n = 9;
    towerOfHanoi(n, 'A', 'C', 'B');
    printf("\n");
    return 0;

}