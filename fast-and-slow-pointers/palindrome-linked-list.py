def isPalindrome(self, head):
    # find middle
    hare, tortoise = head, head
    while hare != None and hare.next != None:
      hare = hare.next.next
      tortoise = tortoise.next

    # reverse linked list from end to middle
    middle = self.reverseList(tortoise)
    start = head

    # check if not equal (doesnt matter if even or odd)
    while middle != None and start != None:
      if middle.val != start.val:
        return False
      middle = middle.next
      start = start.next
    return True

def reverseList(self, head):
    if head == None or head.next == None:
      return head

    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head