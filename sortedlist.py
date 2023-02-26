class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy node to hold the merged list
    dummy = ListNode(0)
    # Create a pointer to the dummy node
    pointer = dummy
    # Loop until either list is exhausted
    while l1 and l2:
        # If the value in list 1 is smaller, add it to the merged list
        if l1.val < l2.val:
            pointer.next = l1
            l1 = l1.next
        # If the value in list 2 is smaller, add it to the merged list
        else:
            pointer.next = l2
            l2 = l2.next
        # Move the pointer to the next node in the merged list
        pointer = pointer.next
    # Add any remaining nodes from list 1 or list 2 to the merged list
    if l1:
        pointer.next = l1
    else:
        pointer.next = l2
    # Return the merged list, skipping the dummy node
    return dummy.next
