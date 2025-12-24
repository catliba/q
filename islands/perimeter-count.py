class Solution:
  def findIslandPerimeter(self, matrix):
    row, col = len(matrix), len(matrix[0])
    count = 0
    for i in range(row):
      for j in range(col):
        if matrix[i][j] == 1:
          count += self.dfs(matrix, i, j)
    return count

  def dfs(self, matrix, x, y):
    row, col = len(matrix), len(matrix[0])
    if x < 0 or y < 0 or x >= row or y >= col:
      return 1
    if matrix[x][y] == 0:
      return 1
    if matrix[x][y] == -1:
      return 0
    if matrix[x][y] == 1:
      matrix[x][y] = -1
    
    down = self.dfs(matrix, x+1, y)
    right = self.dfs(matrix, x, y+1)
    up = self.dfs(matrix, x-1, y)
    left = self.dfs(matrix, x, y-1)

    return left + right + up + down