# Check if two Strings are Anagrams of each other
"""
Given two non-empty strings s1 and s2 of lowercase letters, determine if they are anagrams - i.e., 
if they contain the same characters with the same frequencies.

Examples:

Input: s1 = "geeks"  s2 = "kseeg"
Output: true
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Input: s1 = "allergy", s2 = "allergyy"
Output: false
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. 
Since the frequency of characters differs, the strings are not anagrams.
"""

"""
Approach 1 : Sorting and Comparison - O(n log n + m log m) Time and O(n+m) Space
The idea is that if the strings are anagrams, then their characters will be the same, just rearranged.  

We sort the characters in both strings, the sorted strings will be identical if the original 
strings were anagrams.

We can simply sort the two given strings and compare them - if they are equal, then the original 
strings are anagrams of each other.
"""

def is_anagram_sorting(s1, s2):
    # Sort both strings and compare
    return sorted(s1) == sorted(s2)

"""
Approach 2 : Frequency Counting - O(n + m) Time and O(1) Space
We create a frequency array of size 26 by using characters as index in this array. 

The frequency of ‘a’ is going to be stored at index 0, ‘b’ at 1, and so on. To find the 
index of a character, we subtract character a’s ASCII value from the ASCII value of the character. 
"""

def is_anagram_frequency(s1, s2):
    # If lengths are different, they can't be anagrams
    if len(s1) != len(s2):
        return False

    # Create frequency array for 26 lowercase letters
    freq = [0] * 26

    # Count frequency of each character in both strings
    for i in range(len(s1)):
        freq[ord(s1[i]) - ord('a')] += 1
        freq[ord(s2[i]) - ord('a')] -= 1

    # Check if all frequencies are zero
    return all(count == 0 for count in freq)

"""
Approach 3 : Using HashMap - O(n + m) Time and O(n + m) Space
We can use a hashmap (dictionary) to count the frequency of each character in both strings.
We iterate through the first string and increment the count for each character in the hashmap.
Then, we iterate through the second string and decrement the count for each character in the hashmap.
If the two strings are anagrams, all counts in the hashmap should be zero at the end. 
If any count is not zero, the strings are not anagrams.

Steps

-> First, count the occurrences of each character in the first string using a HashMap.
-> Then, iterate through the second string and decrement the corresponding count for each character 
in the same HashMap.
-> After processing both strings, check the HashMap: if all character counts are zero, the strings 
are anagrams
-> Any non-zero count indicates a mismatch in character frequency, meaning the strings are not anagrams.
"""

def is_anagram_hashmap(s1, s2):
    # If lengths are different, they can't be anagrams
    if len(s1) != len(s2):
        return False

    # Create a hashmap to count character frequencies
    char_count = {}

    # Count frequency of each character in the first string
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement frequency based on the second string
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    # Check if all counts are zero
    return all(count == 0 for count in char_count.values())

"""
In-built Python Function: Using collections.Counter - O(n + m) Time and O(n + m) Space
We can use the built-in Counter class from the collections module to count the frequency of 
characters in both strings and compare the resulting Counter objects. If they are equal, 
the strings are anagrams.
"""

from collections import Counter

def is_anagram_counter(s1, s2):
    return Counter(s1) == Counter(s2)

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"

    result_sorting = is_anagram_sorting(s1, s2)
    result_frequency = is_anagram_frequency(s1, s2)
    result_hashmap = is_anagram_hashmap(s1, s2)
    result_counter = is_anagram_counter(s1, s2)
    print(f"Are '{s1}' and '{s2}' anagrams (using sorting)? {result_sorting}")
    print(f"Are '{s1}' and '{s2}' anagrams (using frequency counting)? {result_frequency}")
    print(f"Are '{s1}' and '{s2}' anagrams (using hashmap)? {result_hashmap}")
    print(f"Are '{s1}' and '{s2}' anagrams (using Counter)? {result_counter}")