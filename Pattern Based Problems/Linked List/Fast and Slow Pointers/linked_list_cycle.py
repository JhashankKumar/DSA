# Finding Loop in a Linked List using Fast and Slow Pointers
"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

"""
Approach:
1. Use two pointers, slow and fast, both initialized to the head of the linked list.
2. Move the slow pointer one step at a time and the fast pointer two steps at a time.
3. If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. If the fast pointer reaches the end of the list (i.e., fast or fast.next is None), then there is no cycle.
4. Return true if the pointers meet, otherwise return false.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    # Create a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create a cycle

    # Check if the linked list has a cycle
    print(hasCycle(head))  # Output: True

    # Create a linked list without a cycle: 1 -> 2
    head2 = ListNode(1)
    head2.next = ListNode(2)

    # Check if the linked list has a cycle
    print(hasCycle(head2))  # Output: False