def sort(self, arr):
    start = 0
    end = len(arr) - 1
    i = 0
    while i < len(arr) and (start < end):
      if arr[i] == 0:
        temp = arr[start]
        if temp == 0:
          continue
        arr[start] = 0
        arr[i] = temp
        start += 1
        i -= 1
      elif arr[i] == 2:
        temp = arr[end]
        if temp == 2 or temp > arr[i]:
          continue
        arr[end] = 2
        arr[i] = temp
        end -= 1
        i -= 1
      i += 1
      print(f"{arr}, {i}, {start}, {end}")
    return arr