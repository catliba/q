from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = {}
        for c in text:
            counter[c] = counter.get(c, 0) + 1
        chars = ['b', 'a','l','o','n']
        for char in chars:
            if char not in counter:
                return 0
        counts = [counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n']]
        return min(counts)