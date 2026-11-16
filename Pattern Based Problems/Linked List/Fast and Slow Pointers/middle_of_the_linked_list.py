# Middle of Linked List
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

"""
Approach:
1. Use two pointers, slow and fast, both initialized to the head of the linked list.
2. Move the fast pointer two steps at a time and the slow pointer one step at a time.
3. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
4. Return the slow pointer.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head) -> ListNode | None:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage:
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Find the middle node
    middle = middleNode(head)

    # Print the values from the middle node to the end
    current = middle
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")