# https://leetcode.com/problems/sqrtx/description/
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        return math.floor(x ** 0.5)