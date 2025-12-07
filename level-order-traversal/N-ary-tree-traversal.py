from collections import deque

# class NAryNode:
#     def __init__(self, val=0, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root):
        result = []
        deq = deque()
        deq.append(root)
        while deq:
            levelSize = len(deq)
            curr = []
            for _ in range(levelSize):
                node = deq.popleft()
                curr.append(node.val)
                for child in node.children:
                    deq.append(child)
            result.append(curr)
        return result