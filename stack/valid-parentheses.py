def isValid(self, s):
    stack = []
    matches = {'(': ')',
               '{': '}',
               '[': ']'
               }
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack.pop() != matches[char]:
                return False
    return not stack