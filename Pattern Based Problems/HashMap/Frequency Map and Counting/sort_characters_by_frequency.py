# Sort Characters by Frequency
"""
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
"""

"""
Approach: HashMap and Sorting Using Heap
1. Use a hash map to count the frequency of each character in the string.
2. Create a max-heap (priority queue) to store the characters based on their frequency.
3. Pop characters from the max-heap and append them to the result string based on their frequency.
4. Return the result string.
"""

def frequency_sort_heap(s):
    from collections import Counter
    import heapq

    # Step 1: Count the frequency of each character using a hash map
    frequency_map = Counter(s)

    # Step 2: Create a max-heap based on the frequency of characters
    max_heap = [(-freq, char) for char, freq in frequency_map.items()]
    heapq.heapify(max_heap)

    # Step 3: Pop characters from the max-heap and build the result string
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char * -freq)  # Append character 'char' 'freq' times

    # Step 4: Return the result string
    return ''.join(result)

if __name__ == "__main__":
    test_cases = [
        ("tree", "eert"),
        ("cccaaa", "aaaccc"),
        ("Aabb", "bbAa")
    ]
    for s, expected in test_cases:
        result = frequency_sort_heap(s)
        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n")