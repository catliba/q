def searchTriplet(self, arr, target_sum):
    sorted_arr = sorted(arr)
    min_dist = float('inf')
    min_target = 0

    for i, x in enumerate(sorted_arr):
        if i > 0 and sorted_arr[i-1] == sorted_arr[i]:
            continue
        start = i + 1
        end = len(sorted_arr) - 1
        while start < end:
            curr_target = sorted_arr[start] + sorted_arr[end] + x
            difference = abs(curr_target - target_sum)
            
            # Update if we found a better (smaller) difference
            if difference < min_dist:
                min_dist = difference
                min_target = curr_target
            # If difference is equal, choose the smaller sum
            elif difference == min_dist:
                min_target = min(min_target, curr_target)
            
            # Moving pointers is seperate from updating the mins
            if curr_target < target_sum:
                start += 1
            else:
                end -= 1
                
    return min_target