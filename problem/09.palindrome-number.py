#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(str(x) == str(x)[::-1]):
            return True

        return False

# @lc code=end
