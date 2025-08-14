class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Read digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check overflow before multiplying and adding
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
