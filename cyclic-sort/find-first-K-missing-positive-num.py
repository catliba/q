def findNumbers(self, nums, k):
    missingNumbers = []
    i = 0
    while i < len(nums):
      j = nums[i] - 1
      # j+1 and not j because we have j as 0 indexing so 0 is technically 1
      if j+1 > 0 and j < len(nums) and nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        i += 1
    counter = 1

    for num in nums:
      if num != counter:
        missingNumbers.append(counter)
        if len(missingNumbers) == k:
          return missingNumbers
      counter += 1
      
    while len(missingNumbers) < k:
      if counter not in nums:
        missingNumbers.append(counter)
      counter += 1 
    return missingNumbers