def nextGreaterElement(self, arr):
    res = [-1]*len(arr)
    stack = []
    for i, num in enumerate(arr):
        while stack and stack[-1][1] < num:
            ptr, val = stack.pop()
            res[ptr] = num
        stack.append((i, num))
    return res