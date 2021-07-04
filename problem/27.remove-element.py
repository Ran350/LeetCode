#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new = []
        for num in nums:
            if(num != val):
                new.append(num)

        # Copy with call by reference
        for i in range(len(new)):
            nums[i] = new[i]

        return len(new)

# @lc code=end
