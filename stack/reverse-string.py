class Solution:
    def reverseString(self, s):
        stack = []
        for char in s:
            stack.append(char)
        rev_str = ""
        while stack:
            rev_str += stack.pop()
        return rev_str
