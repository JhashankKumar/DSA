# Merge Intervals Problem
"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.


Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

"""
Approach: Greedy Algorithm
1. Sort the intervals based on the start time.
2. Initialize an empty list to hold the merged intervals.
3. Iterate through the sorted intervals:
   a. If the merged intervals list is empty or the current interval does not overlap with the last merged interval, append the current interval to the merged list.
   b. If the current interval overlaps with the last merged interval, merge them by updating the end time of the last merged interval to the maximum of the end times of the last merged interval and the current interval.
4. Return the merged intervals list.
"""

def merge_intervals(intervals):
    # Step 1: Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize an empty list to hold the merged intervals
    merged = []

    # Step 3: Iterate through the sorted intervals
    for interval in intervals:
        # If merged is empty or there is no overlap, append the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, merge the current interval with the last one in merged
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

if __name__ == "__main__":
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_intervals(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]

    intervals2 = [[1, 4], [4, 5]]
    print(merge_intervals(intervals2))  # Output: [[1, 5]]

    intervals3 = [[4, 7], [1, 4]]
    print(merge_intervals(intervals3))  # Output: [[1, 7]]