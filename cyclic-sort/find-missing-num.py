class Solution:
  def findMissingNumber(self, nums):
    n = len(nums)
    nums.append(None)
    i = 0
    while i < n+1:
      j = nums[i]
      if j == i:
        i += 1
      elif nums[i] == None:
        i += 1
      else:
        # swap
        nums[j], nums[i] = nums[i], nums[j]
    for x, val in enumerate(nums):
      if val is None:
        return x
    return -1