class Solution:
  def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    start = 0
    end = len(s) - 1
    ss = list(s)
    print(ss)
    while start < end:
      if ss[start] in vowels:
        if ss[end] in vowels:
          temp = ss[start]
          ss[start] = ss[end]
          ss[end] = temp
          start += 1
          end -= 1
        else:
          end -= 1
      else:
        start += 1
    return "".join(ss)