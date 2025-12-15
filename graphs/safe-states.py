class Solution:
    def eventualSafeNodes(self, graph):
        result = []
        visited = [0] * len(graph)
        
        return result
    
    def dfs(self, node, visited):
        if visited[node] == 1:
            return True