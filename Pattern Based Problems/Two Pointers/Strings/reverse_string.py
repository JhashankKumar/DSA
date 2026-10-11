# Reverse a String
"""
Given a string s, reverse the string. Reversing a string means rearranging the characters 
such that the first character becomes the last, the second character becomes second last and so on.

Examples:

Input: s = "GeeksforGeeks"
Output: "skeeGrofskeeG"
Explanation : The first character G moves to last position, the second character e moves to 
second-last and so on.

Input: s = "abdcfe"
Output: "efcdba"
Explanation: The first character a moves to last position, the second character b moves to 
second-last and so on. 

"""

"""
Approach 1: Backward Traversal - O(n) Time and O(n) Space
The idea is to create an empty result string. Then traverse from last character of the given 
string appending each character to the result string. 
"""

def reverse_string_backward_traversal(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result

"""
Approach 2: Two Pointers - O(n) Time and O(1) Space
Start from both ends of the string and keep swapping characters while moving toward the center. 
Each swap places the correct character in its reversed position, and when both pointers meet in 
the middle, the entire string becomes reversed.
"""
def reverse_string_two_pointers(s):
    s = list(s)  # Convert string to list for mutability
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters
        left += 1
        right -= 1

    return ''.join(s)  # Convert list back to string


if __name__ == "__main__":
    test_cases = [
        ("GeeksforGeeks", "skeeGrofskeeG"),
        ("abdcfe", "efcdba"),
        ("hello", "olleh"),
        ("", ""),
        ("a", "a")
    ]
    for s, expected in test_cases:
        result_backward = reverse_string_backward_traversal(s)
        result_two_pointers = reverse_string_two_pointers(s)
        print(f"Input: {s}")
        print(f"Output (Backward Traversal): {result_backward}")
        print(f"Output (Two Pointers): {result_two_pointers}")
        print(f"Expected: {expected}")
        print(f"Test Backward Traversal {'Passed' if result_backward == expected else 'Failed'}")
        print(f"Test Two Pointers {'Passed' if result_two_pointers == expected else 'Failed'}\n")