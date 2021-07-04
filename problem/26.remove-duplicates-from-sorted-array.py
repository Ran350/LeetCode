#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicated = sorted(list(set(nums)))

        # Copy with call by reference
        for i in range(len(duplicated)):
            nums[i] = duplicated[i]

        return len(duplicated)

# @lc code=end
