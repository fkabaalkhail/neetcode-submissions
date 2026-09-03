class Solution:
    def isPalindrome(self, s: str) -> bool:
        # You dont need to introduce an empty array
        l = 0 
        r = len(s) - 1 

        while l < r: 
            while l < r and not s[l].isalnum():
                l += 1 # increment l 

            while r > l and not s[r].isalnum():
                r -= 1 # decrement r 

            if s[l].lower() != s[r].lower():
                return False 

            l += 1 # dont forget to keep checking after
            r -= 1
        return True 
        