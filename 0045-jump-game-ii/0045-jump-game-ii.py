class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        cur_end = 0
        farthest = 0

        for i in range(len(nums) - 1):  # stop before last index
            farthest = max(farthest, i + nums[i])
            if i == cur_end:   # finished current jump range
                jumps += 1
                cur_end = farthest

        return jumps
