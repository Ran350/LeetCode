#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            guess = nums[middle]

            if guess == target:
                return middle

            if guess > target:
                right = middle - 1
            else:
                left = middle + 1

        return left


# @lc code=end
