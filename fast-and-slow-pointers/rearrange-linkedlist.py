class Solution:
  def reverse(self, head):
    if head is None or head.next is None:
      return head

    new_head = self.reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head

  def reorder(self, head):
    # find middle
    tortoise, hare = head, head
    while hare is not None and hare.next is not None:
      hare = hare.next.next
      tortoise = tortoise.next

    # reverse middle - end
    end = self.reverse(tortoise)
    start = head

    # perform insertions
    while start is not None and start.next is not None and end is not None and end.next is not None:
      temp = start.next
      start.next = end
      temp2 = end.next
      end.next = temp
      end = temp2
      start = start.next.next
    return head

# def reorder(self, head):
#     # find middle
#     tortoise, hare = head, head
#     while hare != None and hare.next != None:
#       hare = hare.next.next
#       tortoise = tortoise.next
    
#     start = head
#     while tortoise != None and tortoise.next != None:
#       reverse = tortoise.next.val
#       tortoise.next.val = start.next.val
#       start.next.val = reverse
#       tortoise = tortoise.next.next
#       start = start.next.next
#     return head