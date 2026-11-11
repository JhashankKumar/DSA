# Inser Node at Head, Tail and Nth Position in Linked List
"""
You are given the head of a Singly Linked List and a value x, 
insert that value x at the end of the LinkedList and return the head of the modified Linked List.

Examples :
Input: x = 6,
Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
Explanation: We can see that 6 is inserted at the end of the linkedlist.
   
Input: x = 1,
Output: 4 -> 5 -> 1
Explanation: We can see that 1 is inserted at the end of the linked list.
      
Constraints:
0 ≤ size of linked list, Node.data, x ≤ 105
"""

# At Head
"""
Approach:
1. Create a new node with the given value x.
2. Set the next pointer of the new node to point to the current head of the linked list.
3. Update the head of the linked list to be the new node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertAtHead(head, x):
    new_node = ListNode(x)
    new_node.next = head
    return new_node

# At Tail
"""
Approach:
1. Create a new node with the given value x.
2. If the linked list is empty (head is None), return the new node as the new head.
3. Otherwise, traverse the linked list to find the last node.
4. Set the next pointer of the last node to point to the new node.
"""

def insertAtTail(head, x):
    new_node = ListNode(x)
    if head is None:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# At Nth Position
"""
Approach:
1. Create a new node with the given value x.
2. If the position is 0, insert the new node at the head of the linked list.
3. Otherwise, traverse the linked list to find the node at position n-1.
4. Set the next pointer of the new node to point to the next node of the current node.
5. Set the next pointer of the current node to point to the new node.
6. Return the head of the modified linked list.
"""

def insertAtNthPosition(head, x, n):
    new_node = ListNode(x)
    if n == 0:
        new_node.next = head
        return new_node
    
    current = head
    for _ in range(n - 1):
        if current is None:
            raise IndexError("Position out of bounds")
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head


if __name__ == "__main__":
    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)

    # Insert at head
    head = insertAtHead(head, 0)  # Linked list becomes: 0 -> 1 -> 2 -> 3

    # Insert at tail
    head = insertAtTail(head, 4)  # Linked list becomes: 0 -> 1 -> 2 -> 3 -> 4

    # Insert at nth position
    head = insertAtNthPosition(head, 5, 2)  # Linked list becomes: 0 -> 1 -> 5 -> 2 -> 3 -> 4

    # Print the linked list
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()  # Output: 0 -> 1 -> 5 -> 2 -> 3 -> 4