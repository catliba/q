# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float(-inf)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # case of only 1 or no node:
        if root is None:
            return 0

        self.dfs(root)
        return self.maxSum
    
    def dfs(self, root):
        if root is None:
            return 0
        
        leftSum = max(self.dfs(root.left),0)
        rightSum = max(self.dfs(root.right),0)

        running_sum = leftSum + rightSum + root.val

        self.maxSum = max(self.maxSum, running_sum)
        return root.val + max(leftSum, rightSum)
