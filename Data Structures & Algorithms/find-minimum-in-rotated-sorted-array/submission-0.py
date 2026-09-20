class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r: 
            if nums[l] <= nums[r]: # edge case what if the entire thing is already sorted
                res = min(nums[l], res)
                break
        
            m = (l + r) // 2 ## [3,4,5,6,1,2] = m: 2
            res = min(nums[m], res) ## (5,3) res = 3
            if nums[m] >= nums[l]: # if left is sorted
                    l = m + 1 # move left pointer towards right side since left side is sorted so minimum must be right side 

            else: 
                    r = m - 1 # if right side is sorted move right pointer towards left
            
        return res 


## We don't need to separately check whether the sorted side contains the minimum because we already know what the minimum of a sorted side is when we did res = nums[0]
