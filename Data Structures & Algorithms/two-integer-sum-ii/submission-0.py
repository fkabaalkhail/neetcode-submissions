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
                return [l + 1, r + 1]

                
