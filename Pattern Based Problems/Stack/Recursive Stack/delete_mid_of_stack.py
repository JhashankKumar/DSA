# Delete the middle element of a stack
"""
Given a stack s, delete the middle element of the stack without using any 
additional data structure. The middle element is defined as the floor(size of stack + 1) / 2)-th 
element from the bottom of the stack (using 1-based indexing).

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
Approach: Recursion
1. Use recursion to delete the middle element of the stack.
2. Calculate the middle index of the stack using the formula: mid_index = (len(stack) + 1) // 2.
3. Pop elements from the stack until reaching the middle index, storing them in a temporary variable.
4. Once the middle element is reached, do not push it back onto the stack, effectively deleting it.
5. Push the stored elements back onto the stack in reverse order to maintain the original order of the remaining elements.
6. The recursion will handle the process of popping and pushing elements back onto the stack.
"""

def delete_middle(stack):
    mid_index = (len(stack) + 1) // 2

    def delete_helper(stack, current_index):
        if current_index == mid_index:
            stack.pop()  # Delete the middle element
            return
        item = stack.pop()
        delete_helper(stack, current_index + 1)
        stack.append(item)

    delete_helper(stack, 1)


"""
Alternative Approach: Array Insertion and Removal
1. Use an auxiliary array to store the elements of the stack.
2. Pop all elements from the stack and append them to the auxiliary array.
3. Calculate the middle index of the auxiliary array using the formula: mid_index = (len(auxiliary_array) + 1) // 2.
4. Remove the middle element from the auxiliary array using the pop() method.
5. Push the elements from the auxiliary array back onto the stack in reverse order to maintain the original order of the remaining elements.
6. This approach uses an auxiliary array to temporarily hold the elements of the stack, allowing for easy removal of the middle element.
"""

def delete_middle_with_auxiliary_array(stack):
    auxiliary_array = []
    while stack:
        auxiliary_array.append(stack.pop())
    mid_index = (len(auxiliary_array) + 1) // 2
    auxiliary_array.pop(mid_index - 1)  # Remove the middle element
    for item in reversed(auxiliary_array):
        stack.append(item)

if __name__ == "__main__":
    stack = [10, 20, 30, 40, 50]
    delete_middle(stack)
    print(stack)  # Output: [50, 40, 20, 10]

    stack = [10, 20, 30, 40]
    delete_middle(stack)
    print(stack)  # Output: [40, 30, 10]

    stack = [10, 20, 30, 40, 50]
    delete_middle_with_auxiliary_array(stack)
    print(stack)  # Output: [50, 40, 20, 10]

    stack = [10, 20, 30, 40]
    delete_middle_with_auxiliary_array(stack)
    print(stack)  # Output: [40, 30, 10]