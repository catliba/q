#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def reverse(self, head, k):
    if k < 2:
      return head
    
    # first do one iteration of the reversing and alternating
    start, end = head, head
    for _ in range(k - 1):
      if end == None or end.next == None:
        return self.reverse_linkedlist(start)
      end = end.next
    next_node = end.next
    end.next = None
    new_start = self.reverse_linkedlist(start)
    start.next = next_node
    for _ in range(k):
      if start is None or start.next is None:
        return new_start
      start = start.next

    # prev will be one before the new start segment
    prev = start
    start = start.next
    end = start
    while True:
        # iterate end to appropriate stop location
        for _ in range(k - 1):
            if end == None or end.next == None:
                prev.next = self.reverse_linkedlist(start)
                return new_start
        end = end.next

        # reverse and fix linked list 
        next_node = end.next
        end.next = None
        prev.next = self.reverse_linkedlist(start)
        start.next = next_node
        for _ in range(k):
            if start is None or start.next is None:
                return new_start
        start = start.next
        prev = start
        start = start.next
        end = start

  def reverse_linkedlist(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse_linkedlist(head.next)
        head.next.next = head
        head.next = None
        return new_head