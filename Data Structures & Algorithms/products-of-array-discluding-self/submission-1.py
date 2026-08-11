class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if any one zero, then all zero except that 
        # if any two zero then all zero 

        # brute force - product of whole array
        # then divide by each element 

        # 1 2 4 6
        # 1  1  2 8 prefix
        # 48 24 6 1 suffix

        n = len(nums)
        prefix = [1] * n 
        suffix = [1] * n

        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1] 

        # print(prefix)
        # reverse for loop from n-1 to 0
        for i in range(n-2,-1,-1):
            suffix[i] = nums[i+1] * suffix[i+1]
        # print(suffix)

        sol = [prefix[i] * suffix[i] for i in range(len(nums))]

        return sol


