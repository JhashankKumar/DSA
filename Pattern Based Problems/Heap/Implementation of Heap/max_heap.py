# Max Heap implementation
"""
Implement a class maxHeap that supports the following operations:

push(x) – push element x into the heap
pop() – remove the top element from the heap
peek() – return top element from the heap, if empty return -1
size() - return the no of elements in the heap.
There will be a sequence of queries queries[][]. 
The queries are represented in numeric form:

1 x : call push(x)
2: call pop()
3: call peek()
4: call size()
The driver code will process the queries, call the corresponding functions, 
and print the outputs of peek(), size() operation.

You only need to implement the above four functions.

Examples :

Input: q = 5, queries[][] = [[1, 3], [1, 7], [3], [1, 2], [3]]
Output: [7, 7]
Explanation:
push(3): heap is [3]
push(7): heap is [7, 3]
peek(): return top element 7
push(2): heap is [7, 3, 2]
peek(): return top element 7

Input: q = 6, queries[][] = [[1, 4], [1, 8], [1, 7], [2], [3], [4]]
Output: [7, 2]
Explanation:
push(4): heap is [4]
push(8): heap is [8, 4]
push(7): heap is [8, 7, 4]
pop(): remove top element 8, now heap is [7, 4]
peek(): return top element 7
size(): return no of elements in the heap

Constraints:
1 ≤ q ≤ 103
1 ≤ x ≤ 105
"""

"""
Approach: Max Heap
We can implement the maxHeap class using a min heap data structure by negating the values.
"""

import heapq


class maxHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, -x)

    def pop(self):
        if not self.heap:
            return -1
        return -heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            return -1
        return -self.heap[0]

    def size(self):
        return len(self.heap)


max_heap = maxHeap()
max_heap.push(3)
max_heap.push(7)
print(max_heap.peek())  # Output: 7
max_heap.push(2)
print(max_heap.peek())  # Output: 7

