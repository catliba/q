class Solution:
    def eventualSafeNodes(self, graph):
        def dfs(self, node, visited):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
        
            visited[node] == 1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
            visited[node] = -1
            return True
        result = []
        visited = [0] * len(graph)
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        
        return sorted(result)
    
    