class Solution:
  def floodFill(self, matrix, x, y, newColor):
    n, m = len(matrix[0]), len(matrix)
    
    start = matrix[x][y]

    
    def dfs(matrix,x,y,start):
      if x < 0 or y < 0 or x >= m or y >= n:
        return matrix

      cell = matrix[x][y]
      if cell != start:
        return matrix
      else:
        matrix[x][y] = newColor
      
      dfs(matrix,x+1,y,start)
      dfs(matrix,x,y+1,start)
      dfs(matrix,x-1,y,start)
      dfs(matrix,x,y-1,start)

      return matrix
  
    return dfs(matrix,x,y,start)
  