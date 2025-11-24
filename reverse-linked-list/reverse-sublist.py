class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse_sub_list(self, head, p, q):
        start = Node(0)
        start.next = head
        prev = start
        q_start = start
        p_start = start

        for _ in range(p - 1):
            prev = prev.next
        p_start = prev.next

        for _ in range(q):
            q_start = q_start.next

        rest = q_start.next
        q_start.next = None

        # reverse linked list from p to q
        sublist_head = self.reverse_linked_list(p_start)

        p_start.next = rest
        prev.next = sublist_head
        return start.next

        return head
    def reverse_linked_list(self, head):
        if head is None or head.next is None: 
            return head
        new_head = self.reverse_linked_list(head.next) 
        head.next.next = head 
        head.next = None 
        return new_head