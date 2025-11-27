from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        num_counts = {}
        for num in A:
            num_counts[num] = num_counts.get(num, 0) + 1
        for num in A:
            if num > maxUnique:
                if num_counts[num] == 1:
                    maxUnique = num
        return maxUnique