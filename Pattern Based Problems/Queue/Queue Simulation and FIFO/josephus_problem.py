# Josephus Problem
"""
You are playing a game with n people standing in a circle, numbered from 1 to n. 
Starting from person 1, every kth person is eliminated in a circular fashion. 
The process continues until only one person remains.
Given integers n and k, return the position (1-based index) of the person who will survive.

Examples :
Input: n = 5, k = 2
Output: 3
Explanation: Firstly, the person at position 2 is killed, 
then the person at position 4 is killed, then the person at position 1 is killed. 
Finally, the person at position 5 is killed. So the person at position 3 survives. 

Input: n = 7, k = 3
Output: 4
Explanation: The elimination order is 3 → 6 → 2 → 7 → 5 → 1, and the person at position 4 survives.

Constraints:
1 ≤ n, k ≤ 500
"""

"""
Approach:
1. We can solve the Josephus problem using a recursive approach.
2. The base case is when there is only one person left, in which case the survivor is at position 1.
3. For n > 1, we can find the position of the survivor by recursively calling the function with n-1 and k, and adjusting the result to account for the eliminated person.
4. The final result can be obtained by adding 1 to the result of the recursive call to convert it from 0-based index to 1-based index.
"""

def josephus(n: int, k: int) -> int:
    if n == 1:
        return 1  # Base case: only one person left, survivor is at position 1
    else:
        # Recursive case: find the position of the survivor in the reduced problem
        return (josephus(n - 1, k) + k - 1) % n + 1  # Adjust for eliminated person and convert to 1-based index

"""

"""

if __name__ == "__main__":
    # Test cases
    print(josephus(5, 2))  # Output: 3
    print(josephus(7, 3))  # Output: 4