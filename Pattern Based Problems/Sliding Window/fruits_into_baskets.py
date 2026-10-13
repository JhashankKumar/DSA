# Fruit Into Baskets
"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.

 

Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
 

Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length
"""

"""
Approach: Sliding Window
1. Use a sliding window approach to maintain a window of elements with at most 2 distinct integers (fruit types).
2. Use a hash map to count the frequency of each fruit type in the current window.
3. Expand the window by moving the right pointer and update the count of distinct fruit types.
4. If the count of distinct fruit types exceeds 2, shrink the window from the left until the count of distinct fruit types is at most 2.
5. Keep track of the maximum length of the window during the process, which represents the maximum number of fruits that can be picked.
6. Return the maximum length of the window as the result.
"""
def total_fruit_sliding_window(fruits):
    from collections import defaultdict

    count = 0
    left = 0
    max_fruits = 0
    freq = defaultdict(int)

    for right in range(len(fruits)):
        freq[fruits[right]] += 1

        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

# Example usage:
if __name__ == "__main__":
    fruits1 = [1, 2, 1]
    print(total_fruit_sliding_window(fruits1))  # Output: 3

    fruits2 = [0, 1, 2, 2]
    print(total_fruit_sliding_window(fruits2))  # Output: 3

    fruits3 = [1, 2, 3, 2, 2]
    print(total_fruit_sliding_window(fruits3))  # Output: 4