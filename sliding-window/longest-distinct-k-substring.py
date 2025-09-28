def findLength(self, str1, k):
    max_length = 0
    str_start, str_length = 0, 0
    count = {}
    for str_end in range((str1)):
        if str1[str_end] in count:
          count[str1[str_end]] += 1
        else:
          count[str1[str_end]] = 1
        while len(count) > k:
            count[str1[str_start]] -= 1
            if count[str1[str_start]] == 0:
              del count[str1[str_start]]
        str_start += 1
        max_length = max(max_length, str_end - str_start + 1)
    return max_length