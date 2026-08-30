class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # [[1], [1], [1]]
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i] # updating prefix
        postfix = 1
        for i in range (len(nums) - 1, -1, -1): # range doesnt include stop value which is why we put -1 instead of 0 
            res[i] *= postfix # multiplying prefix and postfix together
            postfix *= nums[i]
        return res





        