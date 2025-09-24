def findMaxSumSubArray(self,k, arr):
    window_sum, window_start = 0, 0
    max_sum = 0
    for window_end in range(len(arr)):
      window_sum += arr[window_end]
      if window_end >= k - 1:
        max_sum = max(window_sum, max_sum)
        window_sum -= arr[window_start]
        window_start += 1
    return max_sum
    