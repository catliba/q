def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# recursive
def reverseList(self, head):
    # base case: empty list or single node
    if head is None or head.next is None:
        return head
    
    # reverse the rest of the list
    new_head = self.reverseList(head.next)
    
    # flip the link
    head.next.next = head
    head.next = None
    
    return new_head

# errors i did: 
# while curr != None and curr.next != None
# return curr
# forgot base case
# initialized curr = head.next, prev = head PREV MUST BE NULL