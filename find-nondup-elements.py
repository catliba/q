def moveElements(self,arr):
    prev = 1
    curr = 1
    while curr < len(arr):
      if arr[curr - 1] != arr[curr]:
        arr[prev] = arr[curr]
        prev = prev + 1
      curr = curr + 1
    return prev