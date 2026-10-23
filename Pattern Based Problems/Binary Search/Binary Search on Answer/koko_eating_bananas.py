# Koko eating bananas problem
"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""

"""
Approach: Binary Search on Answer
1. The minimum eating speed k can be 1 (if Koko eats 1 banana per hour) and the maximum eating speed k can be the maximum number of bananas in any pile (since Koko can eat all bananas in one hour if she chooses the largest pile).
2. We can perform a binary search on the range of possible eating speeds (from 1 to max(piles)).
3. For each mid value of k, we can calculate the total hours needed to eat all the bananas at that speed. If the total hours is less than or equal to h, we can try a smaller eating speed (move the right pointer to mid - 1). If the total hours is greater than h, we need to increase the eating speed (move the left pointer to mid + 1).
4. Continue this process until the left pointer exceeds the right pointer. The left pointer will point to the minimum eating speed k that allows Koko to finish eating all the bananas within h hours.
"""

def min_eating_speed(piles: list[int], h: int) -> int:
    def can_eat_all(k: int) -> bool:
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k  # Equivalent to math.ceil(pile / k)
        return total_hours <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_eat_all(mid):
            right = mid  # Try a smaller eating speed
        else:
            left = mid + 1  # Increase the eating speed

    return left

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([1, 2, 3, 4, 5], 5, 3),
        ([1000000000], 1, 1000000000)
    ]

    for piles, h, expected in test_cases:
        result = min_eating_speed(piles, h)
        print(f"Input: piles = {piles}, h = {h} => Output: {result}, Expected: {expected}") 