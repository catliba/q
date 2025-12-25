from heapq import *

class Solution: 

  def __init__(self):
    self.large, self.small = [], []

  def insertNum(self, num):
    heapify(self.small)
    heappush(self.small, -num) # max heap

    # check if item belongs in large
    if self.small and self.large and (self.small[0] * -1) > self.large[0]:
      val = heappop(self.small) * -1
      heappush(self.large, val)
    
    # check if balanced +-1 
    if len(self.small) < len(self.large) + 1:
      val = heappop(self.small) * -1
      heappush(self.large, val)
    
    if len(self.large) < len(self.small) + 1:
      val = heappop(self.large) 
      heappush(self.small, val)

    return

  def findMedian(self):
    # odd length
    if len(self.small) > len(self.large):
      return self.small[0]
    
    if len(self.small) < len(self.large):
      return self.large[0]
    
    return (self.small[0] + self.large[0]) / 2