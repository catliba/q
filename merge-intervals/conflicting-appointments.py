def canAttendAllAppointments(self, intervals):
    sort = intervals.sort(key=lambda x: x.start)
    # check overlap
    curr = intervals[0].end
    for interval in intervals[1:]:
      if curr > interval.start:
        return False
      curr = interval.end
    return True