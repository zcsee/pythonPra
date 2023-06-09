# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 17:18
 Tool   : PyCharm
 Content: 旋转链表
 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 判断如果传入的k是0或者空链表，以及单节点链表
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head

        # 计算链表的长度
        while cur.next:
            cur = cur.next
            n += 1

        # 如果传入的k值为n的倍数，则返回原链表
        if (add := n - k % n) == n:
            return head

        # 将cur的next指向头节点，形成回环
        cur.next = head

        # 走到要断开的节点上
        while add:
            cur = cur.next
            add -= 1

        # 将新的头节点赋值给到ret
        ret = cur.next
        # 将cur的next指向None，断开链表
        cur.next = None
        return ret


so = Solution()
head_s = so.rotateRight(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))),3)
while head_s:
    print(f"{head_s.val=}")
    head_s = head_s.next
