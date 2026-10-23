# Max Stack Implementation
"""
Implement a class SpecialStack that supports following operations:

push(x) : Insert an integer x onto the stack.
pop() : Remove the top element from the stack.
peek() : Return the top element from the stack. If the stack is empty, return -1.
getMax() : Retrieve the maximum element from the stack in O(1) time. If the stack is empty, return -1.
isEmpty() :  Return true if stack is empty, else false
There will be a sequence of queries queries[][]. The queries are represented in numeric form:

1 x : Call push(x)
2:  Call pop()
3: Call peek()
4: Call getMax()
5: Call isEmpty()
The driver code will process the queries, call the corresponding functions, and print the outputs of peek(), getMax(), isEmpty() operations.
You only need to implement the above five functions.

Examples:
Input: q = 7, queries[][] = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
Output: [3, 2, 2]
Explanation: Queries on stack are as follows:
push(2) into the Stack
push(3) into the Stack
return top of the stack, i.e 3
remove the element 3 from the top of the stack
return maximum element from the stack i.e 2
push(1) into the stack
return maximum element from the stack i.e 2

Input: q = 5, queries[][] = [[1, 4], [1, 2], [4], [3], [5]]
Output: [4, 2, false]
Explanation: Queries on stack are as follows:
push(4) into the Stack
push(2) into the Stack
return maximum element from the stack i.e 4
return top of the stack, i.e 2
stack is non-empty, i.e. return false.

Constraints:
1 ≤ queries.size() ≤ 105
0 ≤ values on the stack ≤ 109
"""

"""
Approach: Use two stacks - one for storing elements and another for tracking maximums.
1. We can use two stacks to implement the SpecialStack. Let's call them stack and max_stack.
2. For the push operation, we can push the new element onto stack. If the new element is greater than or equal to the current maximum (top of max_stack), we also push it onto max_stack.
3. For the pop operation, we pop the top element from stack. If the popped element is equal to the current maximum (top of max_stack), we also pop it from max_stack.
4. For the peek operation, we return the top element of stack. If the stack is empty, we return -1.
5. For the getMax operation, we return the top element of max_stack, which is the current maximum element in the stack. If the stack is empty, we return -1.
6. For the isEmpty operation, we check if the stack is empty and return True or False accordingly.
"""

class SpecialStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self) -> None:
        if self.stack:
            popped_value = self.stack.pop()
            if popped_value == self.max_stack[-1]:
                self.max_stack.pop()

    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMax(self) -> int:
        if self.max_stack:
            return self.max_stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0


stack = SpecialStack()
# Example usage:
queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]
output = []
for query in queries:
    if query[0] == 1:
        stack.push(query[1])
    elif query[0] == 2:
        stack.pop()
    elif query[0] == 3:
        output.append(stack.peek())
    elif query[0] == 4:
        output.append(stack.getMax())
    elif query[0] == 5:
        output.append(stack.isEmpty())
        
print(output)  # Output: [3, 2, 2]