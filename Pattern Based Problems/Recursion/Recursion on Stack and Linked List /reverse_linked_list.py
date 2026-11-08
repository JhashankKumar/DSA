# Reverse Liked List using Recursion
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""

"""
Approach: Use Recursion
1. If the head is None or head.next is None, return head (base case).
2. Recursively call the function with head.next and store the result in a variable (new_head).
3. Set head.next.next to head to reverse the link.
4. Set head.next to None to break the original link.
5. Return new_head as the new head of the reversed list.
"""

def reverse_linked_list(head):
    # Base case: If the list is empty or has only one node, return head
    if head is None or head.next is None:
        return head

    # Recursive case: Reverse the rest of the list
    new_head = reverse_linked_list(head.next)

    # Reverse the link
    head.next.next = head
    head.next = None

    return new_head

if __name__ == "__main__":
    # Example usage
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reverse the linked list
    reversed_head = reverse_linked_list(head)

    # Print the reversed linked list
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")  # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None