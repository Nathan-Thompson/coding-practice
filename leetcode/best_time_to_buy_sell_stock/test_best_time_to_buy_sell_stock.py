#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from unittest import TestCase
from leetcode.best_time_to_buy_sell_stock.best_time_to_buy_sell_stock import Solution


class Test(TestCase):
    def test_solution(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_1(self):
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)

    def test_2(self):
        self.assertEqual(Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]), 2)

    def test_3(self):
        self.assertEqual(Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 4)

    def test_4(self):
        self.assertEqual(Solution().maxProfit([4, 7, 1, 2, 11]), 10)
