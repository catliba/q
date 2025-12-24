from collections import defaultdict

class Solution:
    def validPath(self, n, edges, start, end) -> bool:
        adjacencyList = defaultdict(list)
        # non directed graph 
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)
        visited = [False]*n

        def dfs(curr, visited, end):
            visited[curr] = True
            for neighbor in adjacencyList[curr]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, end)
            return visited[end]

        return dfs(start, visited, end)