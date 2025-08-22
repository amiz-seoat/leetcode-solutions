class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        k = 1  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Found a new unique element
                nums[k] = nums[i]
                k += 1
        
        return k
