from heapq import *

class Job:
 def __init__(self, start, end, cpu_load):
   self.start = start
   self.end = end
   self.cpuLoad = cpu_load

setattr(Job, "__lt__", lambda self, other: self.end < other.end)

class Solution:
    def findMaxCPULoad(self, jobs):
        max_cpu_load = 0
        jobs.sort(key=lambda x: x.start)
        workload = []
        loads = 0
        for job in jobs:
            while workload and job.start >= workload[0].end:
                trash = heappop(workload)
                loads -= trash.cpuLoad
            heappush(workload, job)
            loads += job.cpuLoad
            max_cpu_load = max(loads, max_cpu_load)
        return max_cpu_load