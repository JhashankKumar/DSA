# Non Overlapping Intervals
"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of 
the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. 
For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""

"""
Approach: Greedy Algorithm
1. Sort the intervals based on the end time.
2. Initialize a variable to keep track of the end time of the last added interval and a counter for the number of intervals to remove.
3. Iterate through the sorted intervals:
   a. If the start time of the current interval is greater than or equal to the end time of the last added interval, update the end time to the end time of the current interval.
   b. If the start time of the current interval is less than the end time of the last added interval, increment the counter for the number of intervals to remove. 
4. Return the counter for the number of intervals to remove.
"""

def erase_overlap_intervals(intervals):
    # Step 1: Sort the intervals based on the end time
    intervals.sort(key=lambda x: x[1])

    # Step 2: Initialize variables
    end = float('-inf')
    count = 0

    # Step 3: Iterate through the sorted intervals
    for interval in intervals:
        if interval[0] >= end:
            # No overlap, update the end time
            end = interval[1]
        else:
            # Overlap, increment the counter
            count += 1

    return count

if __name__ == "__main__":
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(erase_overlap_intervals(intervals1))  # Output: 1

    intervals2 = [[1, 2], [1, 2], [1, 2]]
    print(erase_overlap_intervals(intervals2))  # Output: 2

    intervals3 = [[1, 2], [2, 3]]
    print(erase_overlap_intervals(intervals3))  # Output: 0 
