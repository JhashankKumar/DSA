# Sqrt of X
"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 
2 is returned.

Constraints:

0 <= x <= 231 - 1
"""

"""
Approach: Binary Search
1. Initialize two pointers, left and right, to 0 and x respectively
2. While left is less than or equal to right:
   - Calculate the middle index mid as (left + right) // 2
   - If mid * mid is equal to x, return mid (the square root of x)
   - If mid * mid is less than x, move the left pointer to mid + 1 (search in the right half)
   - If mid * mid is greater than x, move the right pointer to mid - 1 (search in the left half)
3. If the square root is not found, return right (the largest integer whose square is less than or equal to x)  
"""

def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            left = mid + 1
        else:
            right = mid - 1
            
    return right

if __name__ == "__main__":
    x = 4
    print(mySqrt(x))  # Output: 2

    x = 8
    print(mySqrt(x))  # Output: 2