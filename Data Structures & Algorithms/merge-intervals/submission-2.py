class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # algorithm 
        # start checking intervals one by one 
        # we want to sort the intervals based on start time first 
        # merged interval - intialised to start and end of interval #1
        # if start of current is less than end of merged then absorb it
        # start is already optimal
        # end is larger or the merged, current's end
        # move to next one 
        # same thing repeats
        # else: 
        # push the currently formed interval into results 
        # initialize this present interval to mergedInterval and proceed in loop
        # return results containing list of lists


        if len(intervals) == 1:
            return intervals

        # sort on start
        # sorted(intervals, key=lambda x: x[0])
        intervals.sort(key=lambda i : i[0])
        print(intervals)

        mergedInterval = []
        results = []

        for interval in intervals:
            if not mergedInterval:
                mergedInterval = interval
                continue
            if interval[0] <= mergedInterval[1]:
                mergedInterval[1] = max(mergedInterval[1], interval[1])
            else:
                results.append(mergedInterval)
                mergedInterval = interval
        
        results.append(mergedInterval)

        return results


