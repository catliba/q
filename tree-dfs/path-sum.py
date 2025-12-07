class Solution:
    def hasPath(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        Lsum = self.hasPath(root.left, sum - root.val)
        Rsum = self.hasPath(root.right, sum - root.val)
        return Lsum or Rsum