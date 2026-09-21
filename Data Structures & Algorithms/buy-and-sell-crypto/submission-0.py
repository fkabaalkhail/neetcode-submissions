class Solution: # Lets use two pointers
    def maxProfit(self, prices: List[int]) -> int:
        l = 0# buy pointer
        r = 1# sell pointer 
        max_profit = 0 
    # We need to make right value bigger than left value to make more profit, buy  low sell high
        while r < len(prices): # so pointer doesnt go out of bound 
            if prices[l] < prices[r]: # if its profitable 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit) # this will change if we get more profit over time 

            else: 
                l = r # move it all way to the right we found lowest price move it we basically found the new minimum 
            r += 1 # no matter what we always want right pointer moving right thats why its indented for the while block 

        return max_profit

