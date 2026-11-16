# Linked List Cycle II
"""
Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
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
4. If the pointers meet, initialize a new pointer, entry, to the head of the linked list. Move both entry and slow one step at a time until they meet. The node where they meet is the start of the cycle.
5. Return the node where entry and slow meet, or return None if there is no cycle.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle(head) -> ListNode | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            return entry

    return None

"""
Alternative Approach:
1. Use a set to keep track of visited nodes.
2. Traverse the linked list, and for each node, check if it is already in the set. If it is, return that node as the start of the cycle. If not, add the node to the set and continue traversing.
3. If the end of the list is reached (i.e., the current node is None), return None as there is no cycle.
4. This approach uses O(n) space, where n is the number of nodes in the linked list.
"""

def detectCycleWithSet(head) -> ListNode | None:
    visited = set()
    current = head

    while current:
        if current in visited:
            return current
        visited.add(current)
        current = current.next

    return None


if __name__ == "__main__":
    # Create a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create a cycle

    # Detect the cycle
    cycle_node = detectCycle(head)

    if cycle_node:
        print(f"Cycle detected at node with value: {cycle_node.val}")
    else:
        print("No cycle detected.")

    # Create a linked list without a cycle: 1 -> 2 -> 3
    head_no_cycle = ListNode(1)
    head_no_cycle.next = ListNode(2)
    head_no_cycle.next.next = ListNode(3)

    # Detect the cycle
    cycle_node_no_cycle = detectCycle(head_no_cycle)

    if cycle_node_no_cycle:
        print(f"Cycle detected at node with value: {cycle_node_no_cycle.val}")
    else:
        print("No cycle detected.")