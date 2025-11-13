# O(n) in place and no extra memory needed
def cyclic_sort(self, nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums