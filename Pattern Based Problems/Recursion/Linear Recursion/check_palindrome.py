# Check Palindrome using Recursion
"""
You are given an integer n. Your task is to find if it is a palindrome.

Examples:
Input: n = 555
Output: true
Explanation: The number 555 reads the same backward as forward, so it is a palindrome.

Input: n = 123
Output: false
Explanation: The number 123 reads differently backward (321), so it is not a palindrome.

Input: n = -121
Output: true
Explanation: if number is palindrome, mainly ignore sign.

Constraints:
-109 ≤ n ≤ 109
"""

"""
Approach:
1. We can solve the problem using a recursive approach.
2. The base case is when the number has only one digit, in which case it is a palindrome.
3. For numbers with more than one digit, we can compare the first and last digits of the number. If they are equal, we can recursively check the remaining digits by removing the first and last digits.
4. If at any point the first and last digits are not equal, we can conclude that the number is not a palindrome.
5. The final result can be obtained by returning true if all comparisons are equal, and false otherwise.
"""

def is_palindrome(n: int) -> bool:
    # Convert the number to a string to easily access its digits
    num_str = str(abs(n))  # Use absolute value to ignore the sign

    # Base case: if the number has only one digit, it is a palindrome
    if len(num_str) <= 1:
        return True

    # Compare the first and last digits
    if num_str[0] != num_str[-1]:
        return False  # Not a palindrome if first and last digits are not equal

    # Recursive case: check the remaining digits by removing the first and last digits
    return is_palindrome(int(num_str[1:-1]))  # Convert back to int for the recursive call

if __name__ == "__main__":
    # Test cases
    print(is_palindrome(555))  # Output: True
    print(is_palindrome(123))  # Output: False
    print(is_palindrome(-121))  # Output: True
    print(is_palindrome(0))  # Output: True
    print(is_palindrome(10))  # Output: False