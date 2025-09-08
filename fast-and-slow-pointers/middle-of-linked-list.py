def findMiddle(self, head):
    tortoise, hare = head, head
    while hare != None and hare.next != None:
      hare = hare.next.next
      tortoise = tortoise.next
    return tortoise