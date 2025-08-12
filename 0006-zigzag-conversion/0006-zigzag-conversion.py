class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # If numRows is 1 or string is too short for zigzag
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        # Iterate through each character and place in correct row
        for char in s:
            rows[curr_row] += char

            # Reverse direction when hitting top or bottom
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            curr_row += 1 if going_down else -1

        # Join all rows together
        return ''.join(rows)
