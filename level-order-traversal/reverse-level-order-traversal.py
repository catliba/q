from collections import deque

class Solution:
    def reverse(self, root):
        result = deque()
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentLevel = []
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.appendleft(currentLevel)
        result = [list(sublist) for sublist in result]
        return result