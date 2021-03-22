class Solution:
    def romanToInt(self, s: str) -> int:
        res, index = 0, len(s)-1
        dd = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # Poping stacka and analyse by rules
        while index >= 0:
            a = s[index]
            if index - 1 < 0: 
                res += dd[a]
            else :
                b = s[index-1]
                if dd[b] >= dd[a]:
                    res += dd[a]
                else:
                    index -= 1
                    res += dd[a] - dd[b]
            index -= 1
        
        return res