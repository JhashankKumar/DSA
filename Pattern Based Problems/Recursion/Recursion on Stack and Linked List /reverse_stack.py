# Reverse a stack using recursion
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
Approach:
1. Create a recursive function to reverse the stack.
2. The base case is when the stack is empty, in which case we return.
3. In the recursive case, pop the top element from the stack and store it in a variable.
4. Recursively call the function to reverse the remaining stack.
5. After the recursive call, insert the stored element at the bottom of the stack.
"""

def reverseStack(st):
    # Base case: If the stack is empty, return
    if not st:
        return
    
    # Pop the top element from the stack
    top_element = st.pop()
    
    # Recursively call the function to reverse the remaining stack
    reverseStack(st)
    
    # Insert the stored element at the bottom of the stack
    insertAtBottom(st, top_element)

def insertAtBottom(st, element):
    # Base case: If the stack is empty, push the element and return
    if not st:
        st.append(element)
        return
    
    # Pop the top element from the stack
    top_element = st.pop()
    
    # Recursively call the function to insert the element at the bottom
    insertAtBottom(st, element)
    
    # Push the stored top element back onto the stack
    st.append(top_element)


def printStack(st):
    # Print the elements of the stack from top to bottom
    for i in range(len(st)-1, -1, -1):
        print(st[i], end=' ')
    print()

if __name__ == "__main__":
    # Test cases
    stack1 = [1, 2, 3, 4]
    print("Original Stack 1:")
    printStack(stack1)
    reverseStack(stack1)
    print("Reversed Stack 1:")
    printStack(stack1)

    stack2 = [3, 2, 1]
    print("Original Stack 2:")
    printStack(stack2)
    reverseStack(stack2)
    print("Reversed Stack 2:")
    printStack(stack2)