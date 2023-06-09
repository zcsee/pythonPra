# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/28 13:18
 Tool   : PyCharm
 Content: 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 栈
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_lst = []
        length = 0
        dummy = ListNode(0, head)
        if head.next is None:
            return head
        while head:
            node_lst.append(head)
            print(f'{head.val=},{head.next=}')
            head = head.next
            length += 1

        inx = length - n

        for i in range(inx):
            node = node_lst.pop(0)
        node.next = node.next.next
        print(f"{node.val=},{node.next.val}")
        return dummy.next

    # 计算链表长度
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        node_lst = []
        dummy = ListNode(0, head)

        length = 0
        if head.next is None:
            return head
        while head:
            node_lst.append(head)
            print(f'{head.val=},{head.next=}')
            head = head.next
            length += 1

        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next

        cur.next = cur.next.next
        print(f"{cur.val=},{cur.next.val}")
        return dummy.next


so = Solution()
so.removeNthFromEnd2(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
# so.removeNthFromEnd(ListNode(1,None),1)
