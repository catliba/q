def isAlienSorted(self, words, order):
    ordering = {}
    for i,char in enumerate(order):
        ordering[char] = i
    
    # Compare words side by side
    for i in range(len(words) - 1):
        for j in range(len(words[i])):
            if j>= len(words[i+1]):
                return False
            if words[i][j] != words[i+1][j]:
                if ordering[words[i][j]] > ordering[words[i+1][j]]: 
                    return False
                break
    return True