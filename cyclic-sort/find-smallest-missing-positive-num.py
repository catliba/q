def findNumber(self, nums):
    i = 0
    hi = len(nums)
    while i < hi:
        j = nums[i] - 1
        if i == j:
            i += 1
        elif j < 0 or j >= hi or nums[i] == nums[j]:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
    counter = 1
    for x in nums:
        if x == None or x != counter:
            return counter
        counter += 1
    return len(nums) + 1