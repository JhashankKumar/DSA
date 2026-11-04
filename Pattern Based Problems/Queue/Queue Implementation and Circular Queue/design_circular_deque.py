# Design Circular Double Ended Queue
"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:
1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""

"""
Approach: Circular Deque Implementation
We can implement a circular deque using an array of fixed size k. We will maintain two pointers, front and rear, to keep track of the front and rear elements of the deque.
The operations will be implemented as follows:
- insertFront(value): If the deque is not full, insert value at the front and update the front pointer. Return true if the operation is successful, else return false.
- insertLast(value): If the deque is not full, insert value at the rear and update  the rear pointer. Return true if the operation is successful, else return false.
- deleteFront(): If the deque is not empty, remove the front element and update the front pointer. Return true if the operation is successful, else return false.
- deleteLast(): If the deque is not empty, remove the rear element and update the rear pointer. Return true if the operation is successful, else return false.
- getFront(): Return the element at the front pointer if the deque is not empty, else return -1.
- getRear(): Return the element at the rear pointer if the deque is not empty, else return -1.
- isEmpty(): Return true if the front pointer is equal to the rear pointer, else return false.
- isFull(): Return true if the next position of the rear pointer is equal to the front pointer, else return false.
"""

class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.deque = [0] * k
        self.front = 0
        self.rear = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.size) % self.size
        self.count -= 1
        return True

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[(self.rear - 1 + self.size) % self.size]
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

if __name__ == "__main__":
    # Example usage
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))  # return True
    print(circularDeque.insertLast(2))  # return True
    print(circularDeque.insertFront(3))  # return True
    print(circularDeque.insertFront(4))  # return False, the deque is full.
    print(circularDeque.getRear())        # return 2
    print(circularDeque.isFull())         # return True
    print(circularDeque.deleteLast())     # return True
    print(circularDeque.insertFront(4))   # return True
    print(circularDeque.getFront())       # return 4