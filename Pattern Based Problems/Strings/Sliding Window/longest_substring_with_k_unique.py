# Longest Substring With k unique Characters

"""
You are given a string s consisting only lowercase alphabets and an integer k. 
Your task is to find the length of the longest substring that contains exactly k 
distinct characters.

Note : If no such substring exists, return -1. 

Examples:
1. Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

2. Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

3. Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.
Constraints:

1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26

"""

"""
Approach: Sliding Window
1. Initialize a dictionary to store the frequency of characters in the current window and two pointers, left and right, to the start of the string.
2. Expand the right pointer to include characters in the current window and update their frequencies.
3. If the number of distinct characters in the window exceeds k, move the left pointer to the right until the number of distinct characters is at most k.
4. Keep track of the maximum length of the substring with exactly k distinct characters during the process.
5. Repeat steps 2-4 until the right pointer reaches the end of the string.
6. Return the maximum length found, or -1 if no such substring exists.
"""

def longest_substring_with_k_unique(s, k):
    from collections import defaultdict
    
    char_count = defaultdict(int)
    left = 0
    max_length = -1
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            
        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)
            
    return max_length

if __name__ == "__main__":  
    s1 = "aabacbebebe"
    k1 = 3
    print(longest_substring_with_k_unique(s1, k1))  # Output: 7

    s2 = "aaaa"
    k2 = 2
    print(longest_substring_with_k_unique(s2, k2))  # Output: -1

    s3 = "aabaaab"
    k3 = 2
    print(longest_substring_with_k_unique(s3, k3))  # Output: 7