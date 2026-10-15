class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''
        1 2 3 4 
        search 4
        brute force O n^2

        l =0, r = len-1 position 
        calculate the sum 
        if its larger than needed - move r behind
        if its smaller than needed - move l ahead
        if it matches - return the indices + 1
        one pass - O(N)
        '''
        # 1 2 3 4 5
        l,r = 0, len(nums)-1

        while(l<r):
            if nums[l] + nums[r] == target:
                return [l+1,r+1]
            elif nums[l] + nums[r] < target:
                l += 1
            else: # nums[l] + nums[r] > target:
                r -= 1
        
        return []



















        # # two pointers 
        # # one at start one at end
        # # if sum big reduce end
        # # if sum small increase start

        # left = 0
        # right = len(numbers)-1

        # while left < right: 
        #     curr = numbers[left] + numbers[right]
        #     if curr == target:
        #         return [left+1, right+1]
        #     elif curr < target:
        #         left += 1
        #     else:
        #         right -= 1
        
        # return []
        