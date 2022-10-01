### Data structure lower-level components 

API is the contract that a data structure (DS) makes with external clients. It includes method definitions, as well as some guarantees about the methods’ behavior that are provided in the DS’s specification. For example, a priority queue (PQ) provides these methods and guarantees:

* top() method returns and extracts the element with the highest priority
* peek() is like top, it returns the element with the highest priority, but without extracting it from the queue
* insert(e, p) adds a new element e with priority p to the PQ
* remove(e) removes element e from the queue
* update(e, p) changes the priority for element e and sets it to p

Invariants (Optional) are internal properties that always hold true throughout the life of the data structure. For instance, a sorted list would have one invariant: every element is not greater than its successor. The purpose of invariants is making sure the conditions necessary to live up to the contract with the external clients are always met. They are the internal counterparts of the guarantees in the API.

Data model hosts the data. This can be a raw chunk of memory, a list, a tree.

Algorithms are the internal logic that is used to update the data structure while making sure that the invariants are not violated.

### Abstract Data Structure and Concrete Data Structure

Abstract Data Structure includes the API and variants, describing at a high level how clients will interact with it and the results and performance of operations.

Concrete Data Structure builds on the principles and API expressed by the abstract description, adding a concrete implementation for its structure and algorithms.

For instance, the relationship between priority queues and heaps. A priority queue is an abstract  data structure that can be implemented in many ways. A head is a concrete implementation of the priority queue using an array to hold elements and specific algorithms to enforce invariants.

### Priority Queue

It behave like a regular queue, plain queue, except that the front of the queue is dynamically determined based on  some kind of priority.

The differences caused to the implementation by the introduction of priority are profound, enough to deserve a special kind of data structure. Generally, a binary heap is the most used version or priority queue.

Binary queue has three invariants:

1. every node has at most two children
2. the heap thee is complete and left-adjusted. Complete means that if the heap has height H, every leaf node is either at level H or H-1. All the levels are left-adjusted, which means that no right sub-tree has a height greater than its left sibling. So, if a leaf is at the same height as an internal node, the leaf can't be on the left of that node. Invariant numbers 1 and 2 are the structural invariants for headp.
3. Every node holds the hoghts priority in the subtree rooted at that node.

Mainly the two formers invariants allow for the array representation of the heap, allowing a representation without pointers to children or parents.

left ith node = (2 * i) + 1;
right ith node = 2 * (i + 1);

parent of a note = (i - 1) / 2

Binary search trees are the most common kind of trees, intrinsically associated with ordering. There is no reason to keep our branching factor fixed and equal to 2. **On the contrary**, **we can use any value greater than 2**, and use the same array representation for the heap.
For a branching factor 3: 
left ith node = (3 * i) + 1;
center ith node = (3 * i) + 2;
right ith node = 3 * (i + 1);

parent of a note = (i - 1) / 3;

For a d-ary heap, where the branching factor is the integer D > 1 , our three heap invariants become

1. Every node has at most D children.
2. The heap tree is complete, with all the levels that are left-adjusted. That is, the i-th sub-tree has a height at most equal to its siblings on its left (from 0 to i-1,1 < i <= D).
3. Every node holds the highest priority in the subtree rooted at that node.

It might seem counterintuitive that we use an array to represent a tree. After all, trees were invented to overcome array limitations. This is generally true, and trees have a number of advantages: they are **more flexible** and, **if balanced**, allow for better performance, **with worst-case logarithmic search, insertion, and delete**.

**As with any data structure that uses pointers** (lists, graphs, trees, and so on) we have a memory **overhead in comparison to arrays**. While with the latter we just need to reserve space for the data (plus maybe, depending on the implementation details, some constant space for pointers and the node structure itself), every tree node requires extra space for the pointers to its children and possibly to its parent.

Arrays also tend to be better at exploiting memory locality: all the elements in the array are contiguous in memory, and this means lower latency when reading them.

### References

LaRocca, Advanced Algorithms And Data Structures, 2021.