def decimalToBinary(self, num):
    stack = []
    while num > 0:
        stack.append(num % 2)
        num = num // 2
    binary = ''
    while stack:
        binary += str(stack.pop())
    return binary
# or
#   return  ''.join(str(i) for i in reversed(stack))