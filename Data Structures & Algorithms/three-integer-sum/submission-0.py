class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: # nums=[-1, 0, 1, 2, -1, -4]
        res = [] # result array 
        nums.sort() # sort all the numbers in the numbers array 

        for i, a in enumerate(nums): # enumerate to get both index and value same time while looping
            if a > 0: # if value greater than 0 
                break

            if i > 0 and a == nums[i - 1]: # we want to check if theres any dups current to prev number but we gotta do a safe check and skip the first index 0 because we would have to do nums[-1] which doesn't make sense this is checking if theres any duplicates
                continue # skip duplicate dont waste time 



            l = i + 1 
            r = len(nums) - 1 

            while l < r: 
                threesum = a + nums[l] + nums[r]

                if threesum > 0: 
                    r -= 1 # move right left to make number smaller

                elif threesum < 0: 
                    l += 1 # make left more right making value bigger

                
                else: # when it does equal 0 

                    res.append([a,nums[l],nums[r]])
                    r -= 1 # dont forget to move after appending value 
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
                
        return res