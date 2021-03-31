class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre, cur, tail = head, head, head
        # Let tail node move n-1 steps firstly
        for i in range(n-1):
            tail = tail.next
        # Then move three pointers until tail.next.next is None
        while tail.next:
            if tail.next.next: 
                # pre move one step less than cur
                pre, cur, tail = pre.next, cur.next, tail.next
            else:
                cur, tail = cur.next, tail.next
        # Judge if to delete head
        if cur == head:
            return head.next        
        # cur node is the node to delete
        pre.next = cur.next

        return head