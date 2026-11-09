# Delete Node from Head, Tail and Nth Position
"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# At Head
"""
Approach:
1. If the head is None, return None.
2. Otherwise, set the head to the next node of the current head.
"""
def deleteAtHead(head):
    if head is None:
        return None
    return head.next

# At Tail
"""
Approach:
1. If the head is None, return None.
2. If the head's next is None, return None (the list has only one node).
3. Otherwise, traverse the linked list to find the second last node.
4. Set the next pointer of the second last node to None, effectively removing the last node.
"""

def deleteAtTail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    
    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None
    return head

# At Nth Position
"""
Approach:
1. Use two pointers, fast and slow, both starting at the head.
2. Move the fast pointer n steps ahead.
3. If the fast pointer reaches the end, it means we need to delete the head node.
4. Otherwise, move both pointers one step at a time until the fast pointer reaches the end.
5. The slow pointer will be at the node just before the one we want to delete.
6. Set the next pointer of the slow pointer to skip the node to be deleted.
"""
def deleteAtNthPosition(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    
    # Move fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Delete the nth node from the end
    slow.next = slow.next.next
    
    return dummy.next

if __name__ == "__main__":
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2
    new_head = deleteAtNthPosition(head, n)

    # Print the modified linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")