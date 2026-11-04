# Design Circular Queue
"""
Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are 
performed based on FIFO (First In First Out) principle, and the last position 
is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces 
in front of the queue. In a normal queue, once the queue becomes full, we cannot 
insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""

"""
Approach: Circular Queue Implementation
We can implement a circular queue using an array of fixed size k. We will maintain two pointers, front and rear, to keep track of the front and rear elements of the queue.
The operations will be implemented as follows:
- enQueue(value): If the queue is not full, insert value at the rear and update the rear pointer. Return true if the operation is successful, else return false.
- deQueue(): If the queue is not empty, remove the front element and update the front pointer. Return true if the operation is successful, else return false.
- Front(): Return the element at the front pointer if the queue is not empty, else return -1.
- Rear(): Return the element at the rear pointer if the queue is not empty, else return -1.
- isEmpty(): Return true if the front pointer is equal to the rear pointer, else return false.
- isFull(): Return true if the next position of the rear pointer is equal to the front pointer, else return false.
"""

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

if __name__ == "__main__":
    # Example usage
    circularQueue = MyCircularQueue(3)
    print(circularQueue.enQueue(1))  # return True
    print(circularQueue.enQueue(2))  # return True
    print(circularQueue.enQueue(3))  # return True
    print(circularQueue.enQueue(4))  # return False
    print(circularQueue.Rear())       # return 3
    print(circularQueue.isFull())     # return True
    print(circularQueue.deQueue())    # return True
    print(circularQueue.enQueue(4))   # return True
    print(circularQueue.Rear())       # return 4