class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Place each number in its right place if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # swap nums[i] into its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find first missing positive
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
    