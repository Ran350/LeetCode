#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        old = None
        while(len(s)):
            s = s.replace("()", "").replace("[]", "").replace("{}", "")

            if(s == old):
                return False

            old = s

        return True
# @lc code=end
