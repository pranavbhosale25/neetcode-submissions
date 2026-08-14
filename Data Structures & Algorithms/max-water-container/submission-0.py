class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # two pointers left and right
        # calculate water 
        # store in a max variable
        # move the smaller bar ahead 
        # do until l < r 

        maxArea = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            maxArea = max(maxArea, (r-l)*min(heights[l], heights[r]))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
        