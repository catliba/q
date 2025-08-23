def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) - 1
    
    while start < end:
      target = arr[start] + arr[end]
      if target == target_sum:
        return [start, end]
      elif target > target_sum:
        end = end - 1
      else:
        start = start + 1
    return [-1,-1]