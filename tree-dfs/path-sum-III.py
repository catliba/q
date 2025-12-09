class Solution:
    def path_sum(self, root, S):
        return self.dfs(root, S, [])

    def dfs(self, node, S, path):
        if node is None:
            return 0
        
        path.append(node.val)
        counter = 0
        for i in range(len(path)):
            curr_sum = path[i:]
            if curr_sum == S:
                counter += 1
        L = self.dfs(node.left, S, path)
        R = self.dfs(node.right, S, path)
        del path[-1]
        return L + R