class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []

        complement = {}
        for i,num in enumerate(nums):
            if (target - num) in complement:
                sol.append(complement[target-num])
                sol.append(i)
                return sol
            else:
                complement[num] = i
                # print(complement)


        return sol
        