class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # If x is less than 2, return itself
        if x < 2 :
            return x
        # Binary Search to find square root
        left, right = 1, x // 2
        while left <= right :
            mid = (left + right) // 2
            if mid * mid > x :
                right = mid - 1
            else : 
                left = mid + 1
        return left - 1