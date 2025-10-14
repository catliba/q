def findPermutation(self, str1, pattern):
    if len(str1) < len(pattern):
      return False

    count = {}
    for c in pattern:
      count[c] = count.get(c, 0) + 1

    matches = 0
    distinct = len(count)
    k = len(pattern)
    
    for i, ch in enumerate(str1):
      if ch in count:
        count[ch] -= 1
        if count[ch] == 0:
          matches += 1

      if i >= k:
        left = str1[i-k]
        if left in count:
          if count[left] == 0:
            matches -= 1
          count[left] += 1
      
      if matches == distinct:
        return True
        
    return False