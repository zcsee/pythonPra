# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 10:56
 Tool   : PyCharm
 Content: 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        # 设置新头
        newhead = head.next
        # 交换 head 和 newhead的位置，并将后续的链表也按照同样方法进行两两交换
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        temp = dummy

        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            # 从 0 1 2 换成 0 2 1
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            # 将temp移动到1的位置，开始下面的判断
            temp = node1
        return dummy

so = Solution()
res = so.swapPairs2(ListNode(1,ListNode(2,ListNode(3,ListNode(4)))))
while res is not None:
    print(res.val)
    res = res.next