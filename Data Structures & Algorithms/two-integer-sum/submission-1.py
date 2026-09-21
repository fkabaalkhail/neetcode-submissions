class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums): ## nums = [3,4,5,6], target = 7 
            diff = target - n # target - key = diff // 7 - 4 = 3 and 3:0 exists
            if diff in indices: #if the difference exists in the key of that value 
                return[indices[diff], i] # return its value 

            indices[n] = i # this is where its getting added to hashmap 
            # ex: {3:0,  }
        

