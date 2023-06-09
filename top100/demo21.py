# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/28 17:04
 Tool   : PyCharm
 Content: 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2 is None:
            return list1
        elif list2 and list1 is None:
            return list2
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)

        pre = prehead

        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            # pre链加了一个节点，所以需要往后移动一个节点
            pre = pre.next
        # 二元判断
        pre.next = list1 if list1 is not None else list2

        return prehead.next


so = Solution()
res = so.mergeTwoLists(ListNode(1, ListNode(2)), ListNode(1, ListNode(3)))
while res:
    print(res.val)
    res = res.next
