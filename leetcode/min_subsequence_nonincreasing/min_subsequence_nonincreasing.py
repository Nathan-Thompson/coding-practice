#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from typing import List

e

class Solution:

    def min_subsequence(self, nums: List[int]) -> List[int]:
        """

        :param self:
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return nums

        total = sum(nums)
        nums.sort(reverse=True)
        for index in range(1, len(nums)+1):

            lowest_nums = sum(nums[:index])
            print(index, lowest_nums)
            if total - lowest_nums < lowest_nums:
                return nums[:index]


x = Solution().min_subsequence(nums=[8, 8])
print(x)