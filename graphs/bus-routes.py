from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        
        queue = deque()
        visited_stops = set()
        used_buses = set()

        queue.append((source, 0)) # 0 for 0 buses taken so far
        visited_stops.add(source)

        while queue:
            current = queue.popleft()
            stop, buses = current[0], current[1]

            for bus in graph:
                continue
            used_buses.add(bus)
            for next_stop in visited_stops:
                visited_stops.add(next_stop)
                queue.append((next_stop, buses + 1))
            
        return -1
