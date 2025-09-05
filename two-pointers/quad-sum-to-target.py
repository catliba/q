def searchQuadruplets(self, arr, target):
    quadruplets = []
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
      if i > 0 and sorted_arr[i] == sorted_arr[i-1]:
        continue
     # perform searchTriplet
      for j in range(i+1, len(arr)):
        start = j+1
        end = len(arr) - 1
        while start < end:
          target_sum = sorted_arr[i] + sorted_arr[j] + sorted_arr[start] + sorted_arr[end]
          if target_sum == target:
            answer_element = sorted([sorted_arr[i], sorted_arr[j], sorted_arr[start], sorted_arr[end]])
            if answer_element not in quadruplets:
              quadruplets.append(answer_element)
            start +=1 
            end -= 1
          elif target_sum < target:
            start += 1
          else:
            end -= 1
    return quadruplets