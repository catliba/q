def compare(self, str1, str2):
    ptr1, ptr2 = len(str1) - 1, len(str2) - 1
    while ptr1 >=0 and ptr2 >= 0:
      ptr1 = self.delete(ptr1, str1)
      ptr2 = self.delete(ptr2, str2)

      if ptr1 < 0 and ptr2 < 0:
        return True
      if ptr1 < 0 or ptr2 < 0:
        return False
      if str1[ptr1] != str2[ptr2]:
        return False

      ptr1 -= 1
      ptr2 -= 1
    return True
  
def delete(self, index, string):
    backspace = 0
    while index >= 0:
      if string[index] == '#':
        backspace += 1
        index -= 1
      elif string[index] != '#' and backspace != 0:
        backspace -= 1
        index -= 1
      else:
        return index
      
    return -1


#  Attempt 1:
# Failed test cases:
# "xp#"
# "xyz##"

# def compare(self, str1, str2):
#     str1 = list(str1)
#     str2 = list(str2)
#     ptr1 = len(str1) - 1
#     ptr2 = len(str2) - 1
#     count1 = 0
#     count2 = 0

#     #base case
#     if ptr1 == 0 and ptr2 == 0:
#       return str1[ptr1] == str2[ptr2]

#     while (ptr1 != 0) and (ptr2 != 0):
#       while str1[ptr1] == '#':
#         count1 += 1
#         ptr1 -= 1
#       while str2[ptr2] == '#':
#         count2 += 1
#         ptr2 -= 1
#       ptr2 = ptr2 - count2
#       ptr1 = ptr1 - count1
#       if ptr2 < 0 or ptr1 < 0:
#       count1 = 0
#       count2 = 0
#       print(f"{str1[ptr1]},{str2[ptr2]}")
#       if str1[ptr1] != str2[ptr2]:
#         return False
#       ptr1 -= 1
#       ptr2 -= 1
#     return True