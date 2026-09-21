class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            cSet = set()
            # Sliding window has two pointers
            l = 0
            res = 0 
            # right pointer will be continiously chaning so we can just use it as 
            for r in range(len(s)):
                while s[r] in cSet: # its a duplicate
                    cSet.remove(s[l]) # remove left most character
                    l += 1
                
                # once we've removed all duplicates 
                cSet.add(s[r])
                res = max(res, r - l + 1) # + 1 because its 0 indexed
            return res 
