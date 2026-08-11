class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # two pointers 
        # one at start one at end
        # if sum big reduce end
        # if sum small increase start

        left = 0
        right = len(numbers)-1

        while left < right: 
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left+1, right+1]
            elif curr < target:
                left += 1
            else:
                right -= 1
        
        return []
        