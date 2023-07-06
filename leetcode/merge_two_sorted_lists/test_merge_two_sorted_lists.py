#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.


from leetcode.merge_two_sorted_lists.merge_two_sorted_lists import Solution, ListNode

solution = Solution()
list_1_head = ListNode(1)
list_1_tail = list_1_head
for val in [2, 4]:
    list_1_tail.next = ListNode(val)
    list_1_tail = list_1_tail.next

list_2_head = ListNode(1)
list_2_tail = list_2_head
for val in [3, 4]:
    list_2_tail.next = ListNode(val)
    list_2_tail = list_2_tail.next


def test_solution():
    new_list_head = Solution().mergeTwoLists(list_1_head, list_2_head)
    ans = []
    while new_list_head is not None:
        ans.append(new_list_head.val)
        new_list_head = new_list_head.next
    assert ans == [1, 1, 2, 3, 4, 4]
