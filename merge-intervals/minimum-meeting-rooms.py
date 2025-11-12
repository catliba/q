import heapq

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
setattr(Meeting, "__lt__", lambda self, other: self.end < other.end)

class Solution:
    def minimum_meeting_rooms(self, meetings):
        meetings.sort(key= lambda x: x.start)

        min_rooms = 0
        min_heap = []
        for meeting in meetings:
            heapq.heappush(min_heap, meeting)
            while min_heap and meeting.start >= min_heap[0].end:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, meeting)
            min_rooms = max(min_rooms, len(min_heap))
        return min_rooms
