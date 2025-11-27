class Solution:
    def longestPalindrome(self, s: str) -> int:      
        length = 0
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        containsOdd = any(v % 2 == 1 for v in counter.values())
        pairs = 0
        for value in counter.values():
            pairs += value // 2
        return pairs*2 + 1 if containsOdd else pairs*2 