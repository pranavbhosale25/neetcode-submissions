class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # base case 
        length = len(nums)
        if length == 0 or length == 1:
            return length

        # we just need to find the start of a sequence 
        numSet = set(nums)
        maxLen = 0;
        for i in numSet:
            if i-1 in numSet:
                # that's not the start!
                continue
            else:
                nextNum = i+1
                while nextNum in numSet:
                    nextNum += 1
                maxLen = max(nextNum - i, maxLen)

        return maxLen
