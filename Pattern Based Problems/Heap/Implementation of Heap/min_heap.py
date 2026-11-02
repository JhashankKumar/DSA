# Min Heap Implementation

"""
Implement a class MinHeap that supports the following operations:

push(x) – push element x into the heap
pop() – remove the top element from the heap
peek() – return top element from the heap, if empty return -1
size() - return the no of elements in the heap.
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : call push(x)
2: call pop()
3: call peek()
4: call size()
The driver code will process the queries, call the corresponding functions, 
and print the outputs of peek(), size() operation.

You only need to implement the above four functions.

Examples :

Input: q = 5, queries[][] = [[1, 3], [1, 7], [3], [1, 2], [3]]
Output: [3, 2]
Explanation:
push(3): heap is [3]
push(7): heap is [3, 7]
peek(): return top element 3
push(2): heap is [2, 3, 7]
peek(): return top element 2

Input: q = 6, queries[][] = [[1, 4], [1, 8], [1, 7], [2], [3], [4]]
Output: [7, 2]
Explanation:
push(4): heap is [4]
push(8): heap is [4, 8]
push(7): heap is [4, 7, 8]
pop(): remove top element 4, now heap is [7, 8]
peek(): return top element 7
size(): return no of elements in the heap

Constraints:
1 ≤ q ≤ 103
1 ≤ x ≤ 105
"""

"""
Approach: Min Heap
We can implement the MinHeap class using a min heap data structure.
"""

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        if not self.heap:
            return -1
        return heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            return -1
        return self.heap[0]

    def size(self):
        return len(self.heap)

heap = MinHeap()
heap.push(3)
heap.push(7)
print(heap.peek())  # Output: 3
heap.push(2)
print(heap.peek())  # Output: 2