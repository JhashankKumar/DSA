# Stack implementation using queue
"""
Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the functions of a 
normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, 
peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. 
You may simulate a queue using a list or deque (double-ended queue) as long as 
you use only a queue's standard operations.
 
Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Follow-up: Can you implement the stack using only one queue?
"""


"""
Approach: Stack using two queues
1. We can use two queues to implement a stack. Let's call them queue1 and queue2.
2. For the push operation, we can enqueue the new element into queue2 and then
   dequeue all elements from queue1 and enqueue them into queue2. Finally, 
   we can swap the names of queue1 and queue2. This way, the new element will be 
   at the front of queue1, and the order of the elements will be maintained.
3. For the pop operation, we can simply dequeue from queue1.
4. For the top operation, we can peek at the front of queue1.
5. For the empty operation, we can check if queue1 is empty.
"""

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue2.append(x)
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue1.pop(0)

    def top(self):
        return self.queue1[0]

    def empty(self):
        return not self.queue1

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
