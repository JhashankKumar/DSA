# Task Scheduler Problem
"""
A geek works in a company and needs to complete a set of tasks given as an array tasks[]. 
The following rules apply:

Completing any task takes exactly one unit of time.
The geek can choose any task that is currently available.
After completing a task, the same task cannot be performed again until at least k time units have passed.  During the cooldown period, the geek can perform other tasks.
If no task is available, the geek can remain idle.

Return the minimum time required to complete all tasks.

Examples:
Input: tasks[] = [1, 1, 1, 2, 2, 2], k = 2
Output: 8
Explanation: One possible schedule is: 1 -> 2 -> idle -> 1 -> 2 -> idle -> 1 -> 2 The same task has a gap of at least 2 time units before it is performed again.

Input: tasks[] = [1, 1, 1, 1, 2, 2, 3, 3], k = 2
Output: 10
Explanation: One possible schedule is: 1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 1 -> 2 -> idle -> 1

Input: tasks[] = [5, 5, 6, 6], k = 0
Output: 4
Explanation: Since the cooldown is 0, the geek can perform the same task immediately. 5 -> 5 -> 6 -> 6

Constraints:
1 ≤ tasks.size() ≤ 104
1 ≤ tasks[i] ≤ 105
0 ≤ k ≤ 100
"""

"""
Approach: Frequency Map and Counting
1. Count the frequency of each task using a hashmap.
2. Find the maximum frequency (max_freq) of any task.
3. Count how many tasks have this maximum frequency (max_count).
4. The minimum time required can be calculated using the formula:
   min_time = (max_freq - 1) * (k + 1) + max_count
5. The result is the maximum of min_time and the total number of tasks,
   because if there are enough tasks to fill the idle slots, the total time will be equal to the number of tasks.
"""

def least_interval(tasks, k):
    from collections import Counter

    # Step 1: Count the frequency of each task
    task_counts = Counter(tasks)
    
    # Step 2: Find the maximum frequency
    max_freq = max(task_counts.values())
    
    # Step 3: Count how many tasks have this maximum frequency
    max_count = sum(1 for count in task_counts.values() if count == max_freq)
    
    # Step 4: Calculate the minimum time required
    min_time = (max_freq - 1) * (k + 1) + max_count
    
    # Step 5: Return the maximum of min_time and the total number of tasks
    return max(min_time, len(tasks))


if __name__ == "__main__":
    tasks = [1, 1, 1, 2, 2, 2]
    k = 2
    print(least_interval(tasks, k))  # Output: 8

    tasks = [1, 1, 1, 1, 2, 2, 3, 3]
    k = 2
    print(least_interval(tasks, k))  # Output: 10

    tasks = [5, 5, 6, 6]
    k = 0
    print(least_interval(tasks, k))  # Output: 4