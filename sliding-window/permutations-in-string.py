# Not a valid sliding window O(n * k)

def findPermutation(self, str1, pattern):
    if len(str1) < len(pattern):
      return False

    count = {}
    for c in pattern:
      count[c] = count.get(c, 0) + 1

    window_len = len(pattern)
    start, end = 0, window_len - 1
    while end < len(str1):
      substr = str1[start:end+1]
      window_count = {}
      for c in substr:
        window_count[c] = window_count.get(c, 0) + 1
      print(substr)
      if count == window_count:
        return True
      start, end = start + 1, end + 1

    return False