class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        Freq = [[] for _ in range (len(nums) + 1)] # its 0 indexed freq = [[], [], [], [], [], [], []]
#                     0   1   2   3   4   5   6

        for n in nums: 
            count[n] = 1 + count.get(n, 0) # add one to the count otherwise give it 0, adding it to count array count = [/,1,2,3,,] value
      #index   0 1 2 3 4  key 
        for n, c in count.items(): # .items() is a method used in python dictonaries where it returns a view of the dictionary key value pairs as tuples 

            Freq[c].append(n) # append the key to the frequency of index count

            #Freq[value] = key
            # Freq[3] comes first because 1:3 
            # Freq = [[], [1], [2], [3], [], [])
        res = []

        for i in range(len(Freq) -1, 0, -1): # 0 indexed so thats why, decrement by -1 
            for n in Freq[i]:
                res.append(n) # if i was 5 append nothing 
                if len(res) == k: # then once we reached k value which here is top 2 we stop and return result
                    return res 



# Count, bucket, then backwards, figure out how many times each number appears, then put each number into bucket matching is frequency line 12 rememver index = frequency then which frequency is the biggest which here is the right so well work backwards



