class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
# Because I only need to know if something exists we'll use a hash set instead of hash map 

        myset = set(nums) # instead of set() you do set(nums) because set() means empty
        res = 0 # we start with an output of 0 
        length = 0 
        for num in myset:  
            if (num - 1) not in myset: # count immediately if before doesnt exist 
                length = 1 # add one to the count 
                while (num + length) in myset: # while 
                    length += 1 
            
            res = max(length, res)

        return res 
