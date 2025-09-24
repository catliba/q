class Solution:
    def loopExists(self, arr):
        n = len(arr)
        if n < 2:
            return False

        def next_idx(i, forward):
            step = arr[i]
            # direction must match
            if (step >= 0) != forward:
                return -1
            # no 1-element self loops
            if step % n == 0:
                return -1
            return (i + step) % n

        for start in range(n):
            forward = arr[start] >= 0
            slow = start
            fast = start

            while True:
                slow = next_idx(slow, forward)
                if slow == -1:
                    break
                fast = next_idx(fast, forward)
                if fast == -1:
                    break
                fast = next_idx(fast, forward)
                if fast == -1:
                    break
                if slow == fast:
                    return True  # found a valid cycle (len >= 2, one direction)

        return False

