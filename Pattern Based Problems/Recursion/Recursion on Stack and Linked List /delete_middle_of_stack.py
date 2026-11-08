# Delete Mid of the Stack
"""
Given a stack s, delete the middle element of the stack without using any additional data structure. 
The middle element is defined as the floor(size of stack + 1) / 2)-th element from the bottom of the stack (using 1-based indexing).

Note: The output shown by the compiler is the stack from top to bottom.

Examples:
Input: s = [10, 20, 30, 40, 50]
Output: [50, 40, 20, 10]
Explanation: The bottom-most element will be 10 and the top-most element will be 50. Middle element will be element at index 3 from bottom, which is 30. Deleting 30, stack will look like [10, 20, 40, 50].

Input: s = [10, 20, 30, 40]
Output: [40, 30, 10]
Explanation: The bottom-most element will be 10 and the top-most element will be 40. Middle element will be element at index 2 from bottom, which is 20. Deleting 20, stack will look like [10, 30, 40].

Constraints:
2 ≤ s.size() ≤ 104
-106 ≤ s[i] ≤ 106
"""

"""
Approach:
1. Calculate the middle index of the stack using the formula: mid = (size of stack + 1) // 2.
2. Use a recursive function to pop elements from the stack until the middle element is reached.
3. When the middle element is reached, do not push it back onto the stack.
4. Push the other elements back onto the stack in the reverse order they were popped.
5. Return the modified stack.
"""

def deleteMiddle(s):
    # Calculate the middle index of the stack
    mid = (len(s) + 1) // 2
    
    def delete_helper(stack, current_index):
        # Base case: if the current index is equal to the middle index, pop the middle element
        if current_index == mid:
            stack.pop()
            return
        
        # Pop the top element and store it
        top_element = stack.pop()
        
        # Recursive call to reach the middle element
        delete_helper(stack, current_index + 1)
        
        # Push the stored element back onto the stack
        stack.append(top_element)
    
    # Start the recursive deletion process from index 1
    delete_helper(s, 1)
    
    return s

if __name__ == "__main__":
    # Example usage
    stack1 = [10, 20, 30, 40, 50]
    print(deleteMiddle(stack1))  # Output: [50, 40, 20, 10]

    stack2 = [10, 20, 30, 40]
    print(deleteMiddle(stack2))  # Output: [40, 30, 10]