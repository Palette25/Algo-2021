# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Function to merge two node lists
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            t0, t1, t2 = dummyHead, head1, head2
            while t1 and t2:
                if t1.val <= t2.val:
                    t0.next = t1
                    t1 = t1.next
                else:
                    t0.next = t2
                    t2 = t2.next
                t0 = t0.next
            if t1:
                t0.next = t1
            elif t2:
                t0.next = t2
            return dummyHead.next

        if head == None:
            return head
        
        dummyHead, tmp = ListNode(0, head), head

        # Sequential Traversal to get node list's length
        length = 0
        while tmp:
            tmp = tmp.next
            length = length + 1
        
        # Here we use half-split methods to perform merge sorting for node list
        subLength = 1 # current split sub-list's length
        
        while subLength < length:
            prev, ptr = dummyHead, dummyHead.next
            while ptr:
                # Get first split of sub-list, length as subLength
                head1 = ptr
                for i in range(1, subLength):
                    if ptr and ptr.next: ptr = ptr.next
                    else: break
                
                # Unlink the first splited sub-list
                head2 = ptr.next
                ptr.next = None
                ptr = head2
                # Get second split of sub-list, length as subLength
                for i in range(1, subLength):
                    if ptr and ptr.next: ptr = ptr.next
                    else: break
                
                # Unlink the second splited sub-list, and record the next node
                forward = None
                if ptr:
                    forward = ptr.next
                    ptr.next = None
                # Merge that two sub-list
                merged = merge(head1, head2)
                # Link the merge result list to prev node
                prev.next = merged
                # Update prev node
                while prev.next:
                    prev = prev.next
                # Update ptr node,
                ptr = forward
            # Update sub-list length, towards next iteration of merging 
            subLength = subLength * 2

        return dummyHead.next