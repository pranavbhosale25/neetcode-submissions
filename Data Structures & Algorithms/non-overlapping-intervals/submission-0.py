class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort on start time
        intervals.sort(key=lambda i: i[0])
        count = 0
        # end of 1st interval
        prevEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= prevEnd:
                prevEnd = intervals[i][1]
            else:
                # overlap! keep the one ending sooner, discard other
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])

        
        return count

