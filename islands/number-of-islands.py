class Solution:
    def countIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        totalIslands = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    # found an island
                    totalIslands += 1
                    self.visit_island_DFS(matrix, i, j)
        return totalIslands

    def visit_island_DFS(self, matrix, x, y):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return
        if (matrix[x][y] == 0):
            return

        self.visit_is_land_DFS(matrix, x + 1, y)
        self.visit_is_land_DFS(matrix, x - 1, y)  
        self.visit_is_land_DFS(matrix, x, y + 1)  
        self.visit_is_land_DFS(matrix, x, y - 1)