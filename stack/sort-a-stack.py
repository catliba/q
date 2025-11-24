# largest elements on top of stack

def sortStack(self, stack):
    tempStack = []
    while len(stack) != 0:
        top = stack.pop()
        while tempStack and tempStack[-1] > top:
            stack.append(tempStack.pop())
        tempStack.append(top)
    return tempStack