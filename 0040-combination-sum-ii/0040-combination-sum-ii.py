class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()  # sort to handle duplicates
        result = []

        def backtrack(start, curr, total):
            if total == target:
                result.append(list(curr))
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicates at same level

                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])  # i+1 (no reuse)
                curr.pop()

                prev = candidates[i]

        backtrack(0, [], 0)
        return result
