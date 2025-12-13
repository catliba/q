class Solution:
    def findProvinces(self, isConnected):
        visited = [False] * len(isConnected)
        count = 0
        for i,n in enumerate(visited):
            if not n:
                self.dfs(i, visited, isConnected)
                count += 1
        return count
    
    # boilerplate dfs code for adjacencyMatrix
    def dfs(self, node, visited, adjacencyMatrix):
        visited[node] = True

        for i, neighbor in enumerate(adjacencyMatrix[node]):
            if not visited[i] and neighbor == 1:
                self.dfs(i, visited, adjacencyMatrix)