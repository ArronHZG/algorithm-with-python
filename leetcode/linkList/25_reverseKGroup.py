import unittest
from typing import List

from utils import stringToListNode, prettyPrintLinkedList, ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        master_head = ListNode(0)  # 保存结果
        master_end = master_head

        p = head  # 负责遍历列表,并计数
        q = head  # 负责保留需要翻转列表的位置, 并复制到master_end

        i = 0
        while p is not None:
            p = p.next
            i += 1
            if i % k == 0:
                tmp = ListNode(0)
                while q is not p:
                    q_next = q.next
                    q.next = tmp.next
                    tmp.next = q
                    q = q_next
                prettyPrintLinkedList(tmp)
                master_end.next = tmp.next
                while master_end.next is not None:
                    master_end = master_end.next
        master_end.next = q
        return master_head.next


class Test(unittest.TestCase):
    def test_one(self):
        s = "[1,2,3,4,5]"
        head = stringToListNode(s)
        prettyPrintLinkedList(head)

        result = Solution().reverseKGroup(head, 3)
        prettyPrintLinkedList(result)
