class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        print(stack)
        output = ""
        stack = list(reversed(stack))
        while stack:
            char, freq = stack.pop()
            for _ in range(freq):
                output += char
        return output