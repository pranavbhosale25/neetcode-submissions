class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solSet = set()
        nums.sort()
        # for loop for i 
        # two pointer approach for j and k 
        # when matched push into solSet and continue (there might be more)


        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    solSet.add((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else: # nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
        
        solList = [list(sol) for sol in solSet]
        return solList
        