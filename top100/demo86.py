# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/13 9:14
 Tool   : PyCharm
 Content: 分隔链表
 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 维护两个链表，用于记录小于目标值和大于等于目标值的两个分链表
        p, q = left, right = ListNode(), ListNode()

        # 原链表的头后续不用，直接用来作为循环的条件
        while head:
            # 如果当前节点的值小于目标值，则加入小链
            if head.val < x:
                left.next = head
                left = left.next
            else:
                # 否则加入大连
                right.next = head
                right = right.next
            head = head.next
        # 将大连的最后一个节点的next设置成None，避免本来后面有小于目标值的节点，形成环
        right.next = None
        # 小连后面接上大连
        left.next = q.next

        return p.next


so = Solution()
hh = so.partition(ListNode(1, ListNode(2, ListNode(4, ListNode(3, ListNode(4, ListNode(2)))))), 3)
# while hh:
#     print(f"{hh.val},{hh.next}")
#     hh = hh.next
