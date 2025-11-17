class Solution:
    def reverse_every_k_element_sublist(self, head, k):
        if k == 1: return head

        prev = head
        end = head
        # this takes end to the end of the first segment
        for _ in range(k - 1):
            if end is None or end.next is None:
                return head
            end = end.next
        next_segment = end.next
        end.next = None

        # reverse the first segment of the linked list
        # this is the start of our returned list
        new_head = self.reverse(prev)

        # now do this for the remaining segments
        while next_segment is not None:
            start = next_segment
            end = next_segment
            for _ in range(k - 1):
                if end is None or end.next is None:
                    prev.next = self.reverse(start)
                    return new_head
            next_segment = end.next
            end.next = None
            prev.next = self.reverse(start)
            prev = start
        return new_head

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head