class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Constants for overflow handling
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Get the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Work with positive numbers
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        # Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quotient += multiple

        # Apply sign
        return -quotient if negative else quotient
