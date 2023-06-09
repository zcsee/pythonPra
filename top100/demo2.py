# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/22 10:48
 Tool   : PyCharm
 Content: 
"""
import collections
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        ans = cur = ListNode()
        while node1 or node2:
            if node1 and node2:
                tmp = node1.val + node2.val
                cur1 = node1.next
                cur2 = node2.next
            if node1:
                pass
            if node2:
                pass