class Solution:
    def countClosedIslands(self, matrix):
        countClosedIslands = 0
        col, row = len(matrix[0]), len(matrix)
        for i in range(row):
            for j in range(col):
                if matrix[i][j] != 0 and self.dfs(matrix, i, j):
                    countClosedIslands += 1
        return countClosedIslands
    
    def dfs(self, matrix, x, y):
        col, row = len(matrix[0]), len(matrix)
        # on border
        if x < 0 or y < 0 or x >= row or y >= col:
            return False
        cell = matrix[x][y]
        if cell == 0:
            return True
        if cell == 1:
            matrix[x][y] = 0
        
        left = self.dfs(matrix, x+1, y)
        right = self.dfs(matrix, x, y+1)
        up = self.dfs(matrix, x-1, y)
        down = self.dfs(matrix, x, y-1)

        return left and right and up and down