class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        pos = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = mul + pos[p2]

                pos[p1] += total // 10
                pos[p2] = total % 10

        # build result string
        result = []
        for p in pos:
            if not (len(result) == 0 and p == 0):  # skip leading zeros
                result.append(str(p))

        return "".join(result)
