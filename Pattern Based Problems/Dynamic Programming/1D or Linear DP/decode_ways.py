# Decode Ways
"""
You have intercepted a secret message encoded as a string of numbers. 
The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different 
ways you can decode the message because some codes are contained in other codes 
("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. 
If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2

Explanation:
"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3

Explanation:
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0

Explanation:
"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

"""
Approach: Dynamic Programming

We can use dynamic programming to solve this problem. Let dp[i] represent the number of ways to decode the substring s[0:i]. 

The recurrence relation is as follows:
- If s[i-1] is a valid single-digit code (1-9), then dp[i] += dp[i-1]
- If s[i-2:i] is a valid two-digit code (10-26), then dp[i] += dp[i-2]

Base cases:
- dp[0] = 1 (empty string has one way to be decoded)
- dp[1] = 1 if s[0] is a valid single-digit code, otherwise 0
"""

def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string
    dp[1] = 1  # Base case: first character is valid

    for i in range(2, n + 1):
        # Check for valid single-digit decode
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Check for valid two-digit decode
        two_digit = int(s[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

if __name__ == "__main__":
    # Test cases
    print(num_decodings("12"))  # Output: 2
    print(num_decodings("226"))  # Output: 3
    print(num_decodings("06"))   # Output: 0
    print(num_decodings("11106")) # Output: 2
    print(num_decodings("10"))   # Output: 1
    print(num_decodings("27"))   # Output: 1