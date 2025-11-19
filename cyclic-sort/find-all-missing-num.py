# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. 
# Find all those missing numbers.

class Solution:
    def findNumbers(self, nums):
        missingNumbers = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if i == j:
                i += 1
            elif nums[i] == nums[j]:
                i += 1
            else:
                nums[j], nums[i] = nums[i], nums[j]
        
        for i, val in enumerate(nums):
            if val != i + 1:
                missingNumbers.append(i+1)
        return missingNumbers