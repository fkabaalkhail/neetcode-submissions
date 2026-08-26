class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newset = set()

        for i in nums:
            if i in newset: 
                return True
            newset.add(i) # sets use .add not .append only for list its append
        else:
            return False 

             
