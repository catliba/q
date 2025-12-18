class Solution:
  def maxAreaOfIsland(self, matrix):
    biggestIslandArea = 0
    m,n = len(matrix), len(matrix[0])

    for i in range(m):
      for j in range(n):
        if matrix[i][j] == 1:
          biggestIslandArea = max(self.dfs(matrix, i, j), biggestIslandArea)

    return biggestIslandArea
  
  def dfs(self, matrix, i, j):
    m,n = len(matrix), len(matrix[0])
    if i < 0 or j < 0 or i >= m or j >= n:
      return 0
    if matrix[i][j] == 0:
      return 0
    else:
      matrix[i][j] = 0

    counter = 1

    counter += self.dfs(matrix, i, j+1)
    counter += self.dfs(matrix, i+1, j)
    counter += self.dfs(matrix, i, j-1)
    counter += self.dfs(matrix, i-1, j)

    return counter