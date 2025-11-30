# monotonic stack because we are looking for the next greater temp day contigiously
class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        output = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx, val = stack.pop()
                output[idx] = i - idx
            stack.append((i, temp))
        return output