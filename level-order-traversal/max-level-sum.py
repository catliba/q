from collections import deque

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root):
        deq = deque()
        deq.append(root)
        max_level = 0
        level = 0
        level_sum = float('-inf')
        while deq:
            curr = []
            level += 1
            levelSize = len(deq)
            for _ in range(levelSize):
                node = deq.popleft()
                curr.append(node.val)
                if node.left is not None:
                    deq.append(node.left)
                if node.right is not None:
                    deq.append(node.right)
            if sum(curr) > level_sum:
                max_level = level
                level_sum = sum(curr)

        return max_level