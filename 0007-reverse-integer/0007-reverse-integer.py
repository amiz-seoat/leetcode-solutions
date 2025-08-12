class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        # Reverse the digits
        reversed_num = 0
        while x_abs != 0:
            digit = x_abs % 10
            x_abs //= 10
            
            # Check for overflow before adding digit
            if (reversed_num > (INT_MAX - digit) // 10):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
