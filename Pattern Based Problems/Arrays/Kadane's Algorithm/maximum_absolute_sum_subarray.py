# Maximum absolute sum of any subarray
"""
You are given an integer array nums. The absolute sum of a subarray 
[numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:
If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

"""
Approach: Kadane's Algorithm for Maximum Absolute Sum of Subarray
1. Initialize four variables: maxsofar, minsofar, currmax, and currmin to 0. 
   - maxsofar will keep track of the maximum absolute sum found so far.
   - minsofar will keep track of the minimum absolute sum found so far.
   - currmax will keep track of the current maximum subarray sum ending at the current position.
   - currmin will keep track of the current minimum subarray sum ending at the current position.
2. Iterate through each number in the input array nums.
   - For each number, update currmax to be the maximum of (currmax + num) and num. This will help in finding the maximum subarray sum ending at the current position.
   - Update maxsofar to be the maximum of maxsofar and currmax. This will keep track of the overall maximum subarray sum found so far.
   - Similarly, update currmin to be the minimum of (currmin + num) and num. This will help in finding the minimum subarray sum ending at the current position.
   - Update minsofar to be the minimum of minsofar and currmin. This will keep track of the overall minimum subarray sum found so far.
3. After iterating through the entire array, return the maximum of maxsofar and the absolute value of minsofar. This will give the maximum absolute sum of any sub  array in the input array nums.
"""
def max_absolute_sum(nums):
    maxsofar = 0
    minsofar = 0
    currmax = 0
    currmin = 0
    
    for num in nums:
        currmax = max(currmax + num, num)
        maxsofar = max(currmax, maxsofar)
        
        currmin = min(currmin + num, num)
        minsofar = min(currmin, minsofar)
    
    return max(maxsofar, abs(minsofar))



if __name__ == "__main__":
    # Example usage
    nums1 = [1, -3, 2, 3, -4]
    print(max_absolute_sum(nums1))  # Output: 5

    nums2 = [2, -5, 1, -4, 3, -2]
    print(max_absolute_sum(nums2))  # Output: 8