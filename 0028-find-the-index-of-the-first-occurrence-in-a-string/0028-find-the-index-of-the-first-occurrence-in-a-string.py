class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0  # Edge case: empty needle is always found at index 0

        # Use Python's built-in find (O(n*m) worst case, but fine for constraints)
        return haystack.find(needle)
