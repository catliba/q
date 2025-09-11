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

# errors i did: 
# while curr != None and curr.next != None
# return curr
# forgot base case
# initialized curr = head.next, prev = head PREV MUST BE NULL