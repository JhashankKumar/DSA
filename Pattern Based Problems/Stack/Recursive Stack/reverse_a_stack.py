# Reverse a stack
"""
You are given a stack st[]. You have to reverse the stack.

Note: The input array represents the stack from bottom to top (last element is the top). 
The output is displayed by printing elements from top to bottom after reversal.

Examples:
Input: st[] = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
Explanation: After reversing, the elements of stack are in opposite order.

Input: st[] = [3, 2, 1]
Output: [3, 2, 1]
Explanation: After reversing, the elements of stack are in opposite order.

Constraints:
1 ≤ st.size() ≤ 100
0 ≤ stack element ≤ 100
"""

"""
Approach: Recursion
1. Use recursion to reverse the stack.
2. Pop the top element of the stack and store it in a variable.
3. Recursively call the reverse function on the remaining stack.
4. Once the stack is reversed, insert the stored element at the bottom of the stack using another recursive function.
5. The insert_at_bottom function will pop elements until the stack is empty, then push the stored element, and finally push back the popped elements in order.
"""

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    if not stack:
        return
    item = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, item)


"""
Approach: Array Insertion and Reversal
1. Use an auxiliary array to store the elements of the stack.
2. Pop all elements from the stack and append them to the auxiliary array.
3. Push the elements from the reversed auxiliary array back onto the stack.
"""

def reverse_stack_with_auxiliary_array(stack):
    auxiliary_array = []
    while stack:
        auxiliary_array.append(stack.pop())
    for item in auxiliary_array:
        stack.append(item)



if __name__ == "__main__":
    stack = [1, 2, 3, 4]
    reverse_stack(stack)
    print(stack)  # Output: [4, 3, 2, 1]

    stack = [3, 2, 1]
    reverse_stack(stack)
    print(stack)  # Output: [1, 2, 3]

    stack = [1, 2, 3, 4]
    reverse_stack_with_auxiliary_array(stack)
    print(stack)  # Output: [4, 3, 2, 1]

    stack = [3, 2, 1]
    reverse_stack_with_auxiliary_array(stack)
    print(stack)  # Output: [1, 2, 3]

