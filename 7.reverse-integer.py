#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
import re


class Solution:
    def reverse(self, x: int) -> int:

        def reverse_digit(s: str) -> str:
            exp = re.compile(r'0+$')
            return re.sub(exp, '',  s[::-1])

        if (x == 0):
            return 0

        if (x > 0):
            reversing_x = int(reverse_digit(str(x)))

            if(2**31 - 1 < reversing_x):
                return 0

            return reversing_x

        if(x < 0):
            reversing_x = int("-" + reverse_digit(str(x)[1:]))

            if(reversing_x < -2**31):
                return 0

            return reversing_x

# @lc code=end
