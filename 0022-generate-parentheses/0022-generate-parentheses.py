class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def backtrack(current, open_count, close_count):
            # If the current string is complete
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add '(' if we still have some left
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add ')' if it won’t break validity
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
