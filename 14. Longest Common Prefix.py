# https://leetcode.com/problems/longest-common-prefix/description/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = strs[0]
        for string in strs:
            while not string.startswith(pre):
                pre = pre[:-1]
        return pre