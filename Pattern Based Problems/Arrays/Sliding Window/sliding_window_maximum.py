# Sliding Window Maximum
"""
Given an array arr[] of positive integers and an integer k. Find the maximum value for 
each contiguous subarray of size k.

Return an array of maximum values corresponding to each contiguous subarray.

Examples : 

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6

Input: arr[] = [5, 1, 3, 4, 2, 6], k = 1
Output: [5, 1, 3, 4, 2, 6]
Explanation: When k = 1, each element in the array is its own subarray, so the output is 
simply the same array.
"""

"""
Approach 1: Using Deque - O(n) Time and O(k) Space
Create a Deque, dq of capacity k, that stores only useful elements of current window of k elements. 
An element is useful if it is in current window and is greater than all other elements on right 
side of it in current window. Process all array elements one by one and maintain dq to contain 
useful elements of current window and these useful elements are maintained in sorted order. 
The element at front of the dq is the largest and element at rear/back of dq is the smallest of 
current window.

Step by Step algorithm
Step 1: Initialize Result List and Deque
res = []
q = deque()
Explanation: We initialize an empty list res to store the results (the maximum values of each sliding window). 
We also initialize a deque q to store elements in a way that allows us to quickly access the maximum element of the current window.

Step 2: Iterate Over the List
for idx, num in enumerate(nums):
Explanation: We iterate over the list nums using enumerate which gives us both the index idx and the current number num. 
This allows us to keep track of the position within the list.

Step 3: Maintain Deque in Descending Order
while q and q[-1] < num:
    q.pop()
q.append(num)
Explanation: For each element in nums:
Inner While Loop: We remove elements from the back of the deque as long as the current element num is greater than the elements in the deque. 
This maintains the deque in a descending order of values.
Append: We append the current element num to the deque.

Step 4: Remove an Element That Is Out of the Current Window
if idx >= k and nums[idx - k] == q[0]:
    q.popleft()
Explanation: If the index idx is greater than or equal to k (indicating that the window has moved forward):
We check if the element at the front of the deque is the same as the element that is now out of the window (i.e., nums[idx - k]).
If it is, we remove this element from the front of the deque (popleft).

Step 5: Append Maximum of Current Window to Result
if idx >= k - 1:
    res.append(q[0])
Explanation: Once the index idx is greater than or equal to k - 1 (indicating that we have processed at least one full window of size k):
We append the element at the front of the deque (q[0]) to the result list res. This element is the maximum value of the current window.

Step 6: Return the Result List
return res
Explanation: After processing all elements in nums, we return the result list res which contains the maximum values for each sliding window.
"""

def sliding_window_maximum(nums, k):
    from collections import deque

    res = []
    q = deque()

    for idx, num in enumerate(nums):
        while q and q[-1] < num:
            q.pop()
        q.append(num)

        if idx >= k and nums[idx - k] == q[0]:
            q.popleft()

        if idx >= k - 1:
            res.append(q[0])

    return res

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1, 4, 5, 2, 3, 6], 3, [3, 3, 4, 5, 5, 5, 6]),
        ([5, 1, 3, 4, 2, 6], 1, [5, 1, 3, 4, 2, 6]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([1], 1, [1])
    ]
    for nums, k, expected in test_cases:
        result = sliding_window_maximum(nums, k)
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'Passed' if result == expected else 'Failed'}\n")