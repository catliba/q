from collections import deque

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Method to find the maximum width of the binary tree
    def widthOfBinaryTree(self, root):
        deq = deque()
        deq.append(root)
        max_width = 0

        while deq:
            levelSize=len(deq)
            curr_width = self.find_max_width(list(deq))
            max_width = max(curr_width, max_width)

            for _ in range(levelSize):
                if deq[0] is None:
                    deq.popleft()
                    continue
                currentNode = deq.popleft()
                if currentNode.left is not None:
                    deq.append(currentNode.left)
                else:
                    deq.append(None)

                if currentNode.right is not None:
                    deq.append(currentNode.right)
                else:
                    deq.append(None)
                
                print([node.val if node else None for node in deq])
        return max_width

    def find_max_width(self, row):
        width_size = len(row)
        if width_size < 2:
            return 1
        i = 0
        j = width_size - 1
        while row[i] is None and i < j:
            i += 1
            width_size -= 1
        while row[j] is None and j >= 0:
            j -= 1
            width_size -= 1
        return width_size