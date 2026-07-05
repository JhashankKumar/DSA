"""
valid palindrome or not

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

def isPalindrome(s: str) -> bool:
    # Convert the string to lowercase and remove non-alphanumeric characters
    filtered_s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the filtered string is equal to its reverse
    return filtered_s == filtered_s[::-1] 

# Example usage
s1 = "A man a plan a canal Panama"
s2 = "race a car"

print(isPalindrome(s1))  # Output: True
print(isPalindrome(s2))  # Output: False