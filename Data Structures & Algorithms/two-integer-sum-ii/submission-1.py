class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l < r: 
            curSum = numbers[l] + numbers[r] # the sum of the two indexes

            if curSum < target: # [1,2,3,4], target = 6
                l += 1 
            
            elif curSum > target: 
                r -= 1 


            else:
                return [l + 1, r + 1] # one indexed


##Use 0-indexing for the pointers because Python lists are 0-indexed. This makes accessing numbers[l] and numbers[r] natural and avoids constantly doing -1.
## 
