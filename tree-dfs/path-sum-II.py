# DFS With Path Tracking (Backtracking Template)
# root-to-leaf path pattern
# def dfs(node, path, results):
#     if node is None:
#         return

#     path.append(node.val)

#     if node.left is None and node.right is None:
#         # leaf reached
#         results.append(list(path))  # copy current path
#     else:
#         dfs(node.left, path, results)
#         dfs(node.right, path, results)
#     path.pop()

#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPaths(self, root, required_sum):
    allPaths = []
    self.dfs(root, required_sum, [], allPaths)
    return allPaths
  
  def dfs(self, node, required_sum, path, result):
    if node is None:
      return
    path.append(node.val)
    if node.val == required_sum and node.left is None and node.right is None:
      result.append(list(path))
    else:
      self.dfs(node.left, required_sum - node.val, path, result)
      self.dfs(node.right, required_sum - node.val, path, result)
    
    del path[-1]