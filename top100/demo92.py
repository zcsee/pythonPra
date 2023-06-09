# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/15 10:12
 Tool   : PyCharm
 Content: 反转链表II
 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        l, r = [], []
        nums = []
        for _ in range(left - 1):
            l.append(head.val)
            head = head.next
        for _ in range(left - 1, right):
            nums.append(head.val)
            head = head.next
        while head:
            r.append(head.val)
            head = head.next

        nn = l + nums[::-1] + r

        head = ListNode(nn[0])
        cur = head
        n = len(nn)
        for i in range(1, n):
            cur.next = ListNode(nn[i])
            cur = cur.next

        return head

    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next


so = Solution()
res = so.reverseBetween2(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)
while res:
    print(f"{res.val=},{res.next=}")
    res = res.next
