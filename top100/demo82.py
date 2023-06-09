# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/12 16:58
 Tool   : PyCharm
 Content: 删除排序链表中的重复元素II
 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
 输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)
        cur = dummy
        # 判断是否有下一个及下下个节点
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val

                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


so = Solution()
hh = so.deleteDuplicates(ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(3, ListNode(4)))))))
while hh:
    print(f"{hh.val=},{hh.next=}")
    hh = hh.next
