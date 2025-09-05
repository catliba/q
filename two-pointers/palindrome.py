def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    ss = list(s)
    start = 0
    end = len(ss) - 1
    while start < end:
      if ss[start].isalpha() or ss[start].isnumeric():
        if ss[end].isalpha() or ss[end].isnumeric():
          if ss[start] == ss[end]:
            start += 1
            end -= 1
          else:
            break
        else:
          end -= 1
      else:
        start += 1
    if start < end:
      return False
    else:
      return True