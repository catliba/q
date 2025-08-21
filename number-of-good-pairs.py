def numGoodPairs(self, nums):
    # get a count of all the number frequencies
    counter = {}
    for num in nums:
      if num not in counter:
        counter[num] = 1
      else:
        counter[num] += 1

    numPairs = 0
    for value in counter.values():
      if value > 1:
        while value != 0:
          value = value - 1
          numPairs += value
    return numPairs