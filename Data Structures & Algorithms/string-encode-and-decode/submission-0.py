class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] 
        for s in strs:
                res.append(str(len(s))) # 4neet get the number 
                res.append("#") # then delimiter
                res.append(s) # then actual string

        return "".join(res) # adds the words without spacing

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # introduce a pointer

        while i < len(s):
            j = i # introduce a second pointer
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # so include numbern not delminiter
            i = j + 1 # we point i after the delimitor
            j = i + length # this will reach the rest of string the length represent the number before delimitor
            res.append(s[i:j])
            i = j # now we back to the next number
        return res 