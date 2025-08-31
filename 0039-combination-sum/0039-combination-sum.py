class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, curr, total):
            if total == target:
                result.append(list(curr))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])  # can reuse same number
                curr.pop()  # undo

        backtrack(0, [], 0)
        return result
