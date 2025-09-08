def hasCycle(self, head):
    hare, tortoise = head, head
    while hare != None and hare.next != None:
      hare = hare.next.next
      tortoise = tortoise.next
      if hare == tortoise:
        return True
    return False

# Improvements: 
# - need to check if hare.next is None before accessing it
# dont need to check if tortoise is None because hare will always be ahead

# def hasCycle(self, head):
#     hare = head
#     tortoise = head
#     while hare != None and tortoise != None:
#       hare = hare.next.next
#       tortoise = tortoise.next
#       if hare == tortoise:
#         return True
#     return False

