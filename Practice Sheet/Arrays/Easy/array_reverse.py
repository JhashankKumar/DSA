"""
Reverse an array arr[]. Reversing an array means rearranging the elements such that 
the first element becomes the last, the second element becomes second last and so on.

Examples:

Input: arr[] = [1, 4, 3, 2, 6, 5]  
Output:  [5, 6, 2, 3, 4, 1]
Explanation: The first element 1 moves to last position, the second element 4 
moves to second-last and so on.

Input: arr[] = [4, 5, 1, 2]
Output: [2, 1, 5, 4]
Explanation: The first element 4 moves to last position, the second element 5 moves 
to second last and so on.
"""

"""
Approach 1:

Naive Approach] Using a temporary array - O(n) Time and O(n) Space

The idea is to use a temporary array to store the reverse of the array.
1. Create a temporary array of same size as the original array. 
2. Now, copy all elements from original array to the temporary array in reverse order.
3. Finally, copy all the elements from temporary array back to the original array.

Time Complexity: O(n), Copying elements to a new array is a linear operation.
Auxiliary Space: O(n), as we are using an extra array to store the reversed array.
"""

def reverse_array_temp(arr):
    n = len(arr)
    temp = [0] * n  # Create a temporary array of same size
    
    # Copy elements in reverse order to the temporary array
    for i in range(n):
        temp[i] = arr[n - 1 - i]
    
    # Copy elements back to the original array
    for i in range(n):
        arr[i] = temp[i]
    
    return arr


"""
[Expected Approach - 1] Using Two Pointers - O(n) Time and O(1) Space
The idea is to maintain two pointers: left and right, such that left points 
at the beginning of the array and right points to the end of the array. 

While left pointer is less than the right pointer, swap the elements at these two positions. 
After each swap, increment the left pointer and decrement the right pointer to move towards 
the center of array. This will swap all the elements in the first half with their corresponding 
element in the second half.
"""

def reverse_array_two_pointers(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move towards the center
        left += 1
        right -= 1
    
    return arr


if __name__ == "__main__":
    arr = [1, 4, 3, 2, 6, 5]

    print("Original array:", arr)

    reversed_arr = reverse_array_temp(arr)
    print("Reversed array using temporary array:", reversed_arr)  # Output: [5, 6, 2, 3, 4, 1]
