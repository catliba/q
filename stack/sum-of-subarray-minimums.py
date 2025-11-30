# monotonic stack
class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        left = [0] * n
        right = [0] * n

        # left
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[i]
            stack.append(i)
        
        # right inclusive
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD
        
        return ans


        
