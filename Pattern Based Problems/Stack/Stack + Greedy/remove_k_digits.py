# Remove K Digits
"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

"""
Approach: Stack
1. Use a stack to keep track of the digits of the number.
2. Iterate through each digit in the string num.
   - While the stack is not empty, k is greater than 0, and the top of the stack is greater than the current digit, pop the top of the stack and decrement k.
3. After processing all digits, if k is still greater than 0, remove the remaining digits from the end of the stack.
4. Construct the result string from the stack, ensuring no leading zeros.
"""

def remove_k_digits(num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k is still greater than 0, remove the remaining digits from the end
    while k > 0:
        stack.pop()
        k -= 1
    
    # Construct the result string and remove leading zeros
    result = ''.join(stack).lstrip('0')
    
    return result if result else '0'

if __name__ == "__main__":
    num = "1432219"
    k = 3
    print(remove_k_digits(num, k))  # Output: "1219"

    num = "10200"
    k = 1
    print(remove_k_digits(num, k))  # Output: "200"

    num = "10"
    k = 2
    print(remove_k_digits(num, k))  # Output: "0"