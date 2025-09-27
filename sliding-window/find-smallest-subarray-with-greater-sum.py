import math
def findMinSubArray(self, s, arr):
    window_sum, window_start = 0,0
    min_length = math.inf
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while s <= window_sum:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    return 0 if min_length == float else min_length