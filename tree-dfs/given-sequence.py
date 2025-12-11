#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):
    return self.dfs(root, sequence, [])
  
  def dfs(self, node, sequence, path):
    if node is None:
      return False
    
    path.append(node.val)
    if path == sequence and node.left is None and node.right is None:
      del path[-1]
      return True
    
    L = self.dfs(node.left, sequence, path)
    R = self.dfs(node.right, sequence, path)
    del path[-1]
    return L or R