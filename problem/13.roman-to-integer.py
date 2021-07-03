#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        symbol = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0

        i = 0
        while(i < len(s)):
            # the case of end of charactor
            if(i == len(s)-1):
                sum += symbol[s[i]]

            # case of written smallest to largest from left to right
            elif(symbol[s[i]] < symbol[s[i+1]]):
                sum += symbol[s[i+1]] - symbol[s[i]]
                i += 1

            else:
                sum += symbol[s[i]]

            i += 1

        return sum
# @lc code=end
