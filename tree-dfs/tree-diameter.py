#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right


class Solution:

  def findDiameter(self, root):
    self.treeDiameter = 0
    diameters = []
    self.dfs(root, diameters)
    return max(diameters)
  
  def dfs(self, node, max_diameter):
    if node is None: 
      return 0
    if node.left is None and node.right is None:
      return 1
    L = self.dfs(node.left, max_diameter)
    R = self.dfs(node.right, max_diameter)
    max_diameter.append(L+R+1)
    return 1 + max(L, R)