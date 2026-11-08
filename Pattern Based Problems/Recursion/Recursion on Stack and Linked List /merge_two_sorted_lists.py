# Merge Two Sorted Linked Lists
"""
ou are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

"""
Approach:
1. Create a dummy node to serve as the starting point of the merged list.
2. Use a pointer to track the current position in the merged list.
3. While both list1 and list2 are not empty:
   a. Compare the values of the current nodes in list1 and list2.
   b. Append the smaller value to the merged list and move the pointer in that list forward.
4. If one of the lists is exhausted, append the remaining nodes of the other list to the merged list.
5. Return the next node of the dummy node, which is the head of the merged list.
"""

def mergeTwoLists(list1, list2):
    # Create a dummy node to serve as the starting point of the merged list
    dummy = ListNode(0)
    current = dummy
    
    # While both lists are not empty
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # If one of the lists is exhausted, append the remaining nodes of the other list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    # Return the next node of the dummy node, which is the head of the merged list
    return dummy.next


if __name__ == "__main__":

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Creating linked lists for testing
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    merged_list = mergeTwoLists(list1, list2)
    
    # Print the merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")