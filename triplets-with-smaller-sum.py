def searchTriplets(self, arr, target):
    count = 0
    arr_sorted = sorted(arr)
    for i in range(len(arr_sorted) - 2):
      for j in range(i+1, len(arr_sorted) - 1):
        ptr = len(arr_sorted) - 1
        while j < ptr:
          print(f"{i},{j},{ptr}")
          trip_sum = arr_sorted[i] + arr_sorted[j] + arr_sorted[ptr]
          if trip_sum < target:
            print(f"Answer: {i},{j},{ptr}")
            count += 1
          ptr -= 1
    return count




# Attempt 1 (Failed)

# def searchTriplets(self, arr, target):
#     count = 0
#     arr_sorted = sorted(arr)
#     for i in range(len(arr_sorted) - 2):
#       start = i+1
#       end = len(arr_sorted) - 1
      
#       while start < end:
#         trip_sum = arr_sorted[i] + arr_sorted[start] + arr_sorted[end]
#         if trip_sum < target:
#           count += 1
#           start += 1
#         elif trip_sum == target:
#           end -= 1
#         else:
#           end -= 1
#     return count