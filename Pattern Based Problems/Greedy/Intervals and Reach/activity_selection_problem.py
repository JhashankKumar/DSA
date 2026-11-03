# Activity Selection Problem
"""
Given two arrays start[] and finish[], where start[i] and finish[i] represent 
the start time and finish time of the i-th activity, find the maximum number of 
activities that a single person can perform.

A person can perform only one activity at a time, and no two selected activities can overlap.
If an activity finishes at time x, the next selected activity must start at a time greater than x.

Examples:

Input: start[] = [1, 3, 0, 5, 8, 5], finish[] = [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: One possible selection is activities {0, 1, 3, 4} with time intervals (1, 2), (3, 4), (5, 7), and (8, 9). 
Each activity starts after the previous one finishes, so a total of 4 activities can be performed.

Input: start[] = [10, 12, 20], finish[] = [20, 25, 30]
Output: 1
Explanation: Activity 0 finishes at time 20, and activity 2 also starts at time 20. 
Since the next activity must start after the previous one finishes, they cannot both be selected. 
Hence, only one activity can be performed.

Constraints:
1 ≤ start.size(), finish.size() ≤ 2*105
0 ≤ start[i], finish[i] ≤ 109
finish.size() = start.size()

"""

"""
Approach: Greedy Algorithm
1. Create a list of pairs (start[i], finish[i]) for each activity.
2. Sort the list of pairs based on the finish times of the activities.
3. Initialize a variable to keep track of the last selected activity's finish time.
4. Iterate through the sorted list of activities:
   a. If the start time of the current activity is greater than or equal to the 
   last selected activity's finish time, select the current activity and update the last 
   selected activity's finish time.  
5. Return the count of selected activities.
"""

def activity_selection_greedy(start, finish):
    # Step 1: Create a list of pairs (start[i], finish[i])
    activities = list(zip(start, finish))
    print(activities)

    # Step 2: Sort the list of pairs based on finish times
    activities.sort(key=lambda x: x[1])
    print(activities)
    # Step 3: Initialize variables
    count = 0
    last_finish_time = -1

    # Step 4: Iterate through the sorted list of activities
    for s, f in activities:
        if s >= last_finish_time:
            count += 1
            last_finish_time = f

    return count

if __name__ == "__main__":
    start1 = [1, 3, 0, 5, 8, 5]
    finish1 = [2, 4, 6, 7, 9, 9]
    print(activity_selection_greedy(start1, finish1))  # Output: 4

    start2 = [10, 12, 20]
    finish2 = [20, 25, 30]
    print(activity_selection_greedy(start2, finish2))  # Output: 1