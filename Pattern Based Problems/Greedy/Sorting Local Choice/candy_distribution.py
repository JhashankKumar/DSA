"""
There are n children standing in a line.

Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

1 <= n == ratings.length <= 5 * 104
0 <= ratings[i] <= 5 * 104
"""

"""
Approach 1: Two Passes - O(n) Time and O(n) Space
1. Create an array candies of the same length as ratings and initialize all elements to 1
2. Traverse the ratings array from left to right. If the current rating is greater than the 
previous rating, increment the current index in candies by 1 more than the previous index.
3. Traverse the ratings array from right to left. If the current rating is greater than the 
next rating, increment the current index in candies by 1 more than the next index.
4. Return the sum of the candies array.
"""

def candy_distribution_greedy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)