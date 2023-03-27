#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/922994739/
from collections import defaultdict
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = defaultdict(int)
        index = 0
        for i in nums:
            unique_nums[i] += 1
            if unique_nums[i] == 1:
                nums[index] = i
                index += 1
        return len(unique_nums)