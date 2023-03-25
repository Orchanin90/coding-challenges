# https://leetcode.com/problems/palindrome-number/description/
# Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:
            return True
        return False
