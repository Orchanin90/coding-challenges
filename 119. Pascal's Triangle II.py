# https://leetcode.com/problems/pascals-triangle-ii/description/

import math as m


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [
            [int(m.factorial(i) / (m.factorial(j) * m.factorial(i - j)))
             for j in range(i + 1)] for i in range(rowIndex + 1)
        ]
        return result.pop(rowIndex)
