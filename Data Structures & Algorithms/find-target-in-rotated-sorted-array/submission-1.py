class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # [1] edge case
        while l <= r: 
            mid = (l + r) // 2 
            if target == nums[mid]:
                return mid 

            # left sorted portion L-mid 
            if nums[mid] >= nums[l]: # if the left side is sorted
                if target > nums[mid] or target < nums[l]: # is the target outside the range of left-mid
                    l = mid + 1
                else: # if the target is in range of the left side 
                    r = mid - 1
            # right sorted portion mid-->right 
            else: 
                if target < nums[mid] or target > nums[r]: # is the target outside the range of mid-right
                    r = mid - 1 
                else:
                    l = mid + 1 
                
        return -1 # if we dont find target in line 9 we exit 
