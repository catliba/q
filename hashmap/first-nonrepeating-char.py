class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for i,c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1
