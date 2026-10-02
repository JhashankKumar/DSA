# Sentence Palindrome
"""
Given a sentence s, determine whether it is a palindrome sentence or not. 
A palindrome sentence is a sequence of characters that reads the same forward and backward after:

-> Converting all uppercase letters to lowercase.
-> Removing all non-alphanumeric characters (i.e., ignore spaces, punctuation, and symbols).
Examples: 

Input: s = "Too hot to hoot."
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters 
to lowercase, string s will become "toohottohoot" which is a palindrome.

Input: s = "Abc 012..##  10cbA"
Output: true
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters 
to lowercase, string s will become "abc01210cba" which is a palindrome.

Input: s = "ABC $. def01ASDF.."
Output: false
Explanation: If we remove all non-alphanumeric characters and convert all uppercase letters 
to lowercase, string s will become "abcdef01asdf" which is not a palindrome.
"""

"""
Approach 1: Normalization and Reverse Check - O(n) Time and O(n) Space
The idea is to preprocess the given sentence by filtering out all non-alphanumeric characters 
and converting all uppercase letters to lowercase. This ensures that the comparison is not 
affected by spaces, punctuation, or letter casing. Once the string is normalized, we simply 
compare it with its reverse. If both are identical, the sentence is a palindrome; otherwise, it is not.
"""

def is_palindrome_sentence_naive_1(s):
    # Normalize the string by filtering out non-alphanumeric characters and converting to lowercase
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]

"""
Approach 2: Two-Pointer Technique - O(n) Time and O(1) Space
This approach uses two pointers to traverse the string from both ends towards the center.
The idea is to use the two-pointer approach to check if a sentence is a palindrome. 
We place one pointer at the start and the other at the end of the string, 
moving them toward each other while comparing characters.
We skip any non-alphanumeric characters and convert uppercase letters to lowercase to 
ensure a case-insensitive comparison. If the characters at both pointers don't match, 
we return false. If the pointers cross without a mismatch, the sentence is a palindrome.
"""

def is_palindrome_sentence_two_pointer(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Move left pointer to the next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer to the previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters at left and right pointers (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        # Move both pointers towards the center
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":
    # Test cases
    test_cases = [
        "Too hot to hoot.",
        "Abc 012..##  10cbA",
        "ABC $. def01ASDF..",
        "A man, a plan, a canal: Panama",
        "No 'x' in Nixon",
        "Not a palindrome"
    ]

    for s in test_cases:
        result = is_palindrome_sentence_naive_1(s)
        print(f"Input: {s}\nOutput: {result}\n")

    for s in test_cases:
        result = is_palindrome_sentence_two_pointer(s)
        print(f"Input: {s}\nOutput: {result}\n")