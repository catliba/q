def findCycleStart(self, head):
    # start at the start and let them meet together
    tort = head.next
    hare = head.next.next
    while tort != hare:
      tort = tort.next
      hare = hare.next.next

    # tort and hare now are on the same node
    # now just start at head again and increment until they meet
    start = head
    while start != tort:
      start = start.next
      tort = tort.next

    return start