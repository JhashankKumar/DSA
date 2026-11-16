# Odd Even Linked List
"""
Given the head of a singly linked list, group all the nodes with odd indices 
together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constraints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
"""

"""
Approach:
1. If the head is None or there is only one node, return the head as it is already in the desired order.
2. Initialize two pointers, odd and even, to point to the first and second nodes of the linked list, respectively. 
Also, keep a reference to the head of the even list (even_head) to connect it later.
3. Iterate through the linked list using a while loop until either the even pointer or the next node of the even pointer is None.
4. Inside the loop, update the next pointer of the odd node to point to the node after the even node (odd.next = even.next). 
Then, move the odd pointer to its next node (odd = odd.next).
5. Update the next pointer of the even node to point to the node after the odd node (even.next = odd.next). 
Then, move the even pointer to its next node (even = even.next).
6. After the loop, connect the last node of the odd list to the head of the even list (odd.next = even_head).
7. Return the head of the modified linked list.
"""

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head

# Example usage:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reorder the linked list
    new_head = oddEvenList(head)

    # Print the reordered linked list
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")