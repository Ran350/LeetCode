#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

import itertools


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for pair in itertools.combinations(range(len(nums)), 2):

            sum = nums[pair[0]] + nums[pair[1]]

            if(sum == target):
                return [pair[0], pair[1]]


# @lc code=end
