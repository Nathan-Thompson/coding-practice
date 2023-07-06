#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

from unittest import TestCase

from valid_parentheses import Solution

solution = Solution()


def test_is_valid():
    assert solution.isValid('()') is True


def test_2():
    assert solution.isValid('{') is False


def test_7():
    assert solution.isValid("()[]{}") == True


def test_3():
    assert solution.isValid("(]") is False


def test_4():
    assert solution.isValid('{[}]') == False


def test_5():
    assert solution.isValid("") == True


def test_6():
    assert solution.isValid('}}}}}}') == False


def test_8():
    assert solution.isValid('{[]}') == True

def test_9():
    assert solution.isValid('((') == False
