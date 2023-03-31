# https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -len(digits)
        for i in range(-1, index - 1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == index:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                return digits
        return digits
