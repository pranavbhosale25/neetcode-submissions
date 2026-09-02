"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort the intervals by start val
        intervals.sort(key= lambda i : i.start)

        endTimes = []

        for interval in intervals:
            if endTimes and endTimes[0] <= interval.start:
                # meeting over, we can fit this in same room
                heapq.heappop(endTimes)
            # push in the end time 
            heapq.heappush(endTimes,interval.end)

        return len(endTimes)


        