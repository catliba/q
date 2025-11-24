# USE SPLIT on / !!!!
def simplifyPath(self, path):
    stack = []
    for p in path.split('/'):
        if p == '..':
            if stack:
                stack.pop()
        # If the component is not empty and not '.', push it onto the stack
        elif p and p != '.':
            stack.append(p)
    return '/' + '/'.join(stack)