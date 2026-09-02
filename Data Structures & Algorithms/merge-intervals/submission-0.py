class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda i : i[0])
        
        output = [intervals[0]]

        for start, end in intervals:
            if output[-1][1] >= start:
                # overlap 
                output[-1][1] = max(end,output[-1][1])
            else:
                output.append([start,end])
        
        return output