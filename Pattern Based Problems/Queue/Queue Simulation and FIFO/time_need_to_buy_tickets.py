# Time need to buy tickets
"""
There are n people in a line queuing to buy tickets, 
where the 0th person is at the front of the line and the (n - 1)th person is 
at the back of the line.

You are given a 0-indexed integer array tickets of length n where the 
number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. 
A person can only buy 1 ticket at a time and has to go back to the 
end of the line (which happens instantaneously) in order to buy more tickets. 
If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person initially at position k (0-indexed) 
to finish buying tickets.

Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6

Explanation:
The queue starts as [2,3,2], where the kth person is underlined.
After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
Continuing this process, the queue becomes [2,1,2] at 2 seconds.
Continuing this process, the queue becomes [1,2,1] at 3 seconds.
Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
Continuing this process, the queue becomes [1,1] at 5 seconds.
Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8

Explanation:
The queue starts as [5,1,1,1], where the kth person is underlined.
After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.
Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.
Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. The kth person has bought all their tickets, so return 8.
 

Constraints:
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
"""

"""
Approach:
1. We can simulate the ticket buying process using a queue.
2. We will use a variable to keep track of the time taken for the person at position k to finish buying tickets.
3. In each iteration, we will check if the person at the front of the queue 
has any tickets left to buy. If they do, we will decrement their ticket count and
increment the time taken. If they have no tickets left, we will remove them from the queue.
4. We will repeat this process until the person at position k has bought all their tickets.
5. Finally, we will return the time taken for the person at position k to finish buying tickets.
"""

def time_needed_to_buy_tickets(tickets: list[int], k: int) -> int:
    time_taken = 0  # Initialize time taken for the person at position k to finish buying tickets
    n = len(tickets)  # Get the number of people in the queue

    while tickets[k] > 0:  # Continue until the person at position k has bought all their tickets
        for i in range(n):  # Iterate through each person in the queue
            if tickets[i] > 0:  # Check if the person has any tickets left to buy
                tickets[i] -= 1  # Decrement their ticket count
                time_taken += 1  # Increment the time taken
            if tickets[k] == 0:  # If the person at position k has bought all their tickets, break out of the loop
                break

    return time_taken  # Return the total time taken for the person at position k to finish buying tickets

if __name__ == "__main__":
    # Test cases
    print(time_needed_to_buy_tickets([2, 3, 2], 2))  # Output: 6
    print(time_needed_to_buy_tickets([5, 1, 1, 1], 0))  # Output: 8