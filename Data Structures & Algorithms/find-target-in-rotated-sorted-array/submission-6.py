class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #    binary search 
    # base cases 
    # if just one element - if its matching - return 0 else -1
    # main task - identifying the pivot 

    # find the pivot
    # do binary search on left of pivot
    # do binary search on right of pivot
    # if any of these two returns non -1 return that 
    # else return -1 

    # 5 6 1 2 3 4 
    #     ^ 

    # 3 4 5 6 1 2 
    #      lm lr   
    # l r 0 len-1
    # mid l+r//2
    # while l < r 
    # if mid > r then pivot is on right
    # if mid < l then pivot current/left 
    # at the end, l ends at pivot

        print("starting exec")
        l = 0
        r = len(nums)-1

        #       l m r     
        # 3 5 6 0 1 2 
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[l] > nums[mid]:
                r = mid
            else:
                r = mid
    
        pivot = l 
        print("found pivot", pivot)

        def binary_search(l:int ,r:int ,nums: List[int],target: int) -> int:
            print(l,"  ", r)
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    r = mid-1
                elif nums[mid] < target:
                    l = mid+1
            print("binary search failed, ret -1")
            return -1

        print("searching left")
        found_in_left = binary_search(0,pivot-1, nums, target)

        if found_in_left != -1:
            return found_in_left

        print("searching right")
        found_in_right = binary_search(pivot,len(nums)-1, nums, target)
        if found_in_right != -1:
            return found_in_right

        return -1 








