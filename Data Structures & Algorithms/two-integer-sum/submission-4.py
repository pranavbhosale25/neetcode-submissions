class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement = {}

        for index,val in enumerate(nums):
            if val in complement:
                return [complement[val],index]
            else:
                complement[target-val] = index
        
        return []
        