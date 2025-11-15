class Interval:
 def __init__(self, start, end):
   self.start = start
   self.end = end

def merge(self, intervals_a, intervals_b):
    result = []
    a,b = 0,0
    while a < len(intervals_a) and b < len(intervals_b):
        interval_a = intervals_a[a]
        interval_b = intervals_b[b]
        # check if overlap; if interval b extends off of a
        if interval_a.end >= intervals_b.start and interval_a.start <= interval_b.start:
            start = max(interval_a.start, interval_b.start)
            end = min(interval_a.end, interval_b.end)
            result.append(Interval(start,end))
        # b contains trailing a
        elif interval_b.start <= interval_a.start and interval_b.end >= interval_a.start:
            start = max(interval_a.start, interval_b.start)
            end = min(interval_a.end, interval_b.end)
            result.append(Interval(start,end))
        
        # increment whichever one is the smallest end
        if interval_a.end < interval_b.end:
            a += 1
        else:
            b += 1
        return result