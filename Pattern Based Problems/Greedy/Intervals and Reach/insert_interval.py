# Insert Interval
"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order 
by starti. You are also given an interval newInterval = [start, end] that represents the 
start and end of another interval.

Two intervals are considered overlapping if they share at least one point.

Insert newInterval into intervals such that intervals is still sorted in ascending order 
by starti and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

"""
Approach: Greedy Algorithm
1. Initialize an empty list to hold the result intervals.
2. Iterate through the existing intervals:
   a. If the current interval ends before the new interval starts, add it to the result.
   b. If the current interval starts after the new interval ends, add the new interval to the result and update the new interval to the current interval.
   c. If the current interval overlaps with the new interval, merge them by updating the start to the minimum of both starts and the end to the maximum of both ends.
3. After the loop, add the last new interval to the result.
4. Return the result list.
"""

def insert_interval(intervals, new_interval):
    result = []
    for interval in intervals:
        if interval[1] < new_interval[0]:
            # Current interval ends before new interval starts, add it to result
            result.append(interval)
        elif interval[0] > new_interval[1]:
            # Current interval starts after new interval ends, add new interval to result
            result.append(new_interval)
            new_interval = interval  # Update new_interval to current interval
        else:
            # Overlapping intervals, merge them
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    
    # Add the last new interval to the result
    result.append(new_interval)
    return result

if __name__ == "__main__":
    intervals1 = [[1, 3], [6, 9]]
    new_interval1 = [2, 5]
    print(insert_interval(intervals1, new_interval1))  # Output: [[1, 5], [6, 9]]

    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval2 = [4, 8]
    print(insert_interval(intervals2, new_interval2))  # Output: [[1, 2], [3, 10], [12, 16]]