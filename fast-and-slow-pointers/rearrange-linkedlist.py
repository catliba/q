def reorder(self, head):
    # find middle
    tortoise, hare = head, head
    while hare != None and hare.next != None:
      hare = hare.next.next
      tortoise = tortoise.next
    
    start = head
    while tortoise != None and tortoise.next != None:
      reverse = tortoise.next.val
      tortoise.next.val = start.next.val
      start.next.val = reverse
      tortoise = tortoise.next.next
      start = start.next.next
    return head