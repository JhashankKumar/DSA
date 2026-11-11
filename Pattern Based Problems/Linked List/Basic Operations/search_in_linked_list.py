# Search in a linked list
"""
Given the head of a singly linked list and an integer key, 
check if the key is present in the linked list or not.

Example:
Input: key = 3,
Output: true 
Explanation: 3 is present in Linked List.

Input: key = 4,
Output: false
Explanation: 4 is not present in Linked List.

Constraints:
1 ≤ size of linked list, key ≤ 105
"""

"""
Approach:
1. Traverse the linked list starting from the head node.
2. For each node, compare its value with the key.
3. If a match is found, return true.
4. If the end of the linked list is reached without finding a match, return false.
"""

def searchInLinkedList(head, key):
    # Traverse the linked list
    current = head
    while current:
        # Check if the current node's value matches the key
        if current.val == key:
            return True
        current = current.next
    
    # If the end of the list is reached without finding the key, return False
    return False

if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Example usage:
    # Creating a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    key_to_search = 3
    result = searchInLinkedList(head, key_to_search)
    print(f"Is {key_to_search} present in the linked list? {result}")

    key_to_search = 5
    result = searchInLinkedList(head, key_to_search)
    print(f"Is {key_to_search} present in the linked list? {result}")