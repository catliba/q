class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


# Long Way
class Solution:
  def insert(self, intervals, new_interval):
    # Edge case: empty
    if not intervals:
      return [new_interval]

    # 1) Build a single list with new_interval inserted ONCE in order
    inserted = False
    ordered = []
    for iv in intervals:
      if not inserted and new_interval.start < iv.start:
        ordered.append(new_interval)
        inserted = True
      ordered.append(iv)
    if not inserted:
      ordered.append(new_interval)

    # 2) Merge the ordered list
    merged = []
    start, end = ordered[0].start, ordered[0].end
    for iv in ordered[1:]:
      if iv.start <= end:                # overlap
        end = max(end, iv.end)
      else:                              # no overlap, push previous
        merged.append(Interval(start, end))
        start, end = iv.start, iv.end
    merged.append(Interval(start, end))
    return merged
  
# Better solution:
# move pointer to the instance where insert interval start is not greater than end of interval i
# for intervals that overlap, we employ min max between the two intervals
# add the rest of intervals where start i is larger than end of insert