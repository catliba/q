def containsDuplicate(self, nums):
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            return True
    unique_nums.add(num)
    return False