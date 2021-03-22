class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        while x :
            pop = x % 10 if x > 0 else x % (-10)
            x = x // 10 if x > 0  else int(x/10)
            
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > INT_MAX % 10):
                return 0
            if res < int(INT_MIN / 10) or (res == int(INT_MIN / 10) and pop < INT_MIN % -10):
                return 0
            res = res * 10 + pop
        
        return res