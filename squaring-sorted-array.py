def makeSquares(arr):
    n = len(arr)
    answer = [0 for x in range(n)]

    start = 0
    end = len(arr) - 1
    descending = len(answer) - 1

    while start != end:
      sqrt_start = arr[start] ** 2
      sqrt_end = arr[end] ** 2
      if sqrt_start > sqrt_end:
        answer[descending] = sqrt_start
        start = start + 1
      else:
        answer[descending] = sqrt_end
        end = end - 1
      descending = descending - 1
    # last iteration not completed so we manually do it
    answer[descending] = arr[start] ** 2
    return answer