# monotonic stack because we look for next greater element in a linked list
class Solution:
    def removeNodes(self, head):
        start, end = head, head
        stack = []
        while end != None:
            while stack and end.val > stack[-1].val:
                remove = stack.pop()
                if stack:
                    stack[-1].next = end
                else:
                    start = end
            stack.append(end)
            end = end.next
        return start