def insert(self, intervals, new_interval):
    merged = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(len(intervals)):
      interval = intervals[i]
      print(f"start: {start}, end: {end}")
      # 6 scenarios
      # no overlap // 2 cases
      if end < new_interval.start or start > new_interval.end:
        merged.append(Interval(start, end))
        start = interval.start
        end = interval.end
      # interval overlaps new_interval where interval starts before new_interval and new_interval trails
      if end > new_interval.start and new_interval.end > end:
        start = interval.start
        end = new_interval.end
      # if interval contains new_interval
      if start < new_interval.start and end > new_interval.end:
        return [intervals]
      # if overlap where new_interval starts before interval and interval trails:
      if new_interval.start < start and end > new_interval.end:
        start = new_interval.start
        end = interval.end
      # if interval is contained by new_interval
      if start > new_interval.start and end < new_interval.end:
        start = min(start, new_interval.start)
        end = max(end, new_interval.end)
    merged.append(Interval(start, end))
    return merged