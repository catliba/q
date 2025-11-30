class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num): return "0"
        if k == 0: return num

        stack = []
        for i, integer in enumerate(num):
            while stack and stack[-1] > int(integer):
                stack.pop()
                k = k - 1
                if k == 0:
                    return str(int("".join(str(i) for i in stack) + num[i:]))
            stack.append(int(integer))
        return str(int("".join(str(i) for i in stack[0:len(stack)-k])))