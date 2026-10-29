# Insert at bottom of stack
"""
Given a stack st containing n integers and an integer x, insert x at the bottom of the stack.

Note: While displaying the stack, the bottommost element is printed first.

Examples :
Input: st = [4, 3, 2, 1, 8], x = 2
Output: [2, 4, 3, 2, 1, 8]
Explanation: After insertion of 2, the final stack will be [2,4,3,2,1,8].

Input: st = [5, 3, 1], x = 4
Output: [4, 5, 3, 1]
Explanation: After insertion of 4, the final stack will be [4,5,3,1].

Constraints:
1 ≤ n ≤ 105
0 ≤ x, elements of stack ≤ 109
"""

"""
Approach: Recursion
1. Use recursion to insert the element x at the bottom of the stack.
2. If the stack is empty, push x onto the stack.
3. If the stack is not empty, pop the top element and store it in a temporary variable.
4. Recursively call the function to insert x at the bottom of the stack.
5. After the recursive call, push the stored element back onto the stack to maintain the original order of the elements.
6. The recursion will handle the process of popping and pushing elements back onto the stack, allowing x to be inserted at the bottom.
"""

def insert_at_bottom(stack, x):
    if not stack:
        stack.append(x)
        return
    temp = stack.pop()
    insert_at_bottom(stack, x)
    stack.append(temp)


"""
Alternative Approach: Array Insertion
1. Use an auxiliary array to store the elements of the stack.
2. Pop all elements from the stack and append them to the auxiliary array.
3. Append x to the auxiliary array.
4. Push the elements from the auxiliary array back onto the stack in reverse order to maintain the original order of the elements.
5. This approach uses an auxiliary array to temporarily hold the elements of the stack, allowing for easy insertion of x at the bottom.
"""

def insert_at_bottom_with_auxiliary_array(stack, x):
    auxiliary_array = []
    while stack:
        auxiliary_array.append(stack.pop())
    auxiliary_array.append(x)
    for item in reversed(auxiliary_array):
        stack.append(item)

if __name__ == "__main__":
    stack = [4, 3, 2, 1, 8]
    x = 2
    insert_at_bottom(stack, x)
    print(stack)  # Output: [2, 4, 3, 2, 1, 8]

    stack = [5, 3, 1]
    x = 4
    insert_at_bottom(stack, x)
    print(stack)  # Output: [4, 5, 3, 1]

    stack = [4, 3, 2, 1, 8]
    x = 2
    insert_at_bottom_with_auxiliary_array(stack, x)
    print(stack)  # Output: [2, 4, 3, 2, 1, 8]

    stack = [5, 3, 1]
    x = 4
    insert_at_bottom_with_auxiliary_array(stack, x)
    print(stack)  # Output: [4, 5, 3, 1]