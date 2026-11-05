# Find the winner of a circular game where players are eliminated in a fixed step size until only one remains.
"""
There are n friends that are playing a game. 
The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, 
and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. 
The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, 
go back to step 2 starting from the friend immediately clockwise of the friend 
who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

Example 1:
Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Example 2:
Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.
 
Constraints:
1 <= k <= n <= 500
 
Follow up:
Could you solve this problem in linear time with constant space?
"""

"""
Approach:
1. We can simulate the game using a list to represent the friends in the circle.
2. We will use a variable to keep track of the current index in the list.
3. In each iteration, we will calculate the index of the friend to be eliminated using the formula: (current_index + k - 1) % len(friends).
4. We will remove the friend at that index from the list and update the current index to be the next friend in the circle.
5. We will repeat this process until only one friend remains in the list.
"""

def find_the_winner(n: int, k: int) -> int:
    friends = list(range(1, n + 1))  # Create a list of friends numbered from 1 to n
    current_index = 0  # Start at the first friend

    while len(friends) > 1:
        # Calculate the index of the friend to be eliminated
        current_index = (current_index + k - 1) % len(friends)
        # Remove the friend from the circle
        friends.pop(current_index)

    return friends[0]  # Return the last remaining friend as the winner

if __name__ == "__main__":
    # Example usage
    n = 5
    k = 2
    print(find_the_winner(n, k))  # Output: 3

    n = 6
    k = 5
    print(find_the_winner(n, k))  # Output: 1