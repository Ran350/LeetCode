#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isSameElement(l: list) -> bool:
            return l == [l[0]] * len(l) if l else False

        if(not strs):
            return ""

        if("" in strs):
            return ""

        # In case there is no prefix match
        if(not isSameElement([s[0] for s in strs])):
            return ""

        # In case there is prefix match
        shortest_element = min(strs, key=lambda s: len(s))

        for i in range(len(shortest_element)):
            l = [str[:i+1] for str in strs]

            if(not isSameElement(l)):
                return shortest_element[:i]

        return shortest_element


# @lc code=end
