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