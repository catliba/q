class Interval:
 def __init__(self, start, end):
   self.start = start
   self.end = end

 def print_interval(self):
   print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge_intervals(self, intervals):
    mergedInterval = []
    
    intervals.sort(key=lambda x: x.start)

    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        # overlap boundaries are inclusive
        if interval.start <= end:
            end = max(interval.end, end)
        # no overlap
        else:
            mergedInterval.append(Interval(start,end))
            start = interval.start
            end = interval.end

    mergedInterval.append(Interval(start,end))  
    return mergedInterval
