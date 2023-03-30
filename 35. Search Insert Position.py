# https://leetcode.com/problems/search-insert-position/description/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid_index = len(nums) // 2
        low_index = 0
        high_index = len(nums) - 1
        while nums[mid_index] != target and low_index <= high_index:
            if nums[mid_index] > target:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
            mid_index = (low_index + high_index) // 2
        if low_index > high_index:
            return low_index
        return mid_index
