def sort(self, arr):
    start = 0
    end = len(arr) - 1
    i = 0
    while i <= end:
      print(f"{arr}, {i}, {end}")
      if arr[i] == 1:
        i += 1
      elif arr[i] == 0:
        # swap
        temp = arr[i]
        arr[i] = arr[start]
        arr[start] = temp
        i += 1
        start += 1
      else:
        temp = arr[i]
        arr[i] = arr[end]
        arr[end] = temp
        end -= 1
    return arr

#Attempt 1 - Failed

# def sort(self, arr):
#     start = 0
#     end = len(arr) - 1
#     i = 0
#     while i < len(arr) and (start < end):
#       if arr[i] == 0:
#         temp = arr[start]
#         if temp == 0:
#           continue
#         arr[start] = 0
#         arr[i] = temp
#         start += 1
#         i -= 1
#       elif arr[i] == 2:
#         temp = arr[end]
#         if temp == 2 or temp > arr[i]:
#           continue
#         arr[end] = 2
#         arr[i] = temp
#         end -= 1
#         i -= 1
#       i += 1
#       print(f"{arr}, {i}, {start}, {end}")
#     return arr

#Attempt 2 - Failed

# def sort(self, arr):
#     start = 0
#     end = len(arr) - 1
#     i = 0
#     while i < end:
#       if arr[i] == 1:
#         i += 1
#       elif arr[i] == 0:
#         # swap
#         temp = arr[i]
#         arr[i] = arr[start]
#         arr[start] = temp
#         i += 1
#         start += 1
#       else:
#         temp = arr[i]
#         arr[i] = arr[end]
#         arr[end] = temp
#         end -= 1
      
#     return arr