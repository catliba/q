def searchTriplets(arr):
    triplets = []

    # sort array
    sorted_arr = sorted(arr)

    # start at left, and treat it as a pair with target sum problem
    for i,x in enumerate(sorted_arr):
      #don't forget to skip duplicates (uniqueness)
      if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
        continue
      target_sum = x * -1
      start = i+1
      end = len(sorted_arr) - 1
      while start < end:
        if sorted_arr[start] + sorted_arr[end] == target_sum:
          triplets.append([x, sorted_arr[start], sorted_arr[end]])
          start += 1
          end -= 1
          while start < end and sorted_arr[start] == sorted_arr[start - 1]:
            start += 1
          while start < end and sorted_arr[end] == sorted_arr[end + 1]:
            end -= 1
        elif sorted_arr[start] + sorted_arr[end] > target_sum:
          end = end - 1
        else:
          start = start + 1
    return triplets
