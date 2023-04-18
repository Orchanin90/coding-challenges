# https://leetcode.com/problems/pascals-triangle/description/

import math as m


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return [
            [int(m.factorial(i) / (m.factorial(j) * m.factorial(i - j)))
             for j in range(i + 1)]
            for i in range(numRows)
        ]
