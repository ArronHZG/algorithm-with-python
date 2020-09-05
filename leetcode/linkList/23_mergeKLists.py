import heapq
import math
import unittest
from typing import List

from utils import stringToListNode, prettyPrintLinkedList, ListNode


def get_min_node(first_nodes):
    min_val = math.inf
    index = -1

    for i in range(len(first_nodes)):
        if first_nodes[i].val < min_val:
            index = i
            min_val = first_nodes[i].val

    return index


class SolutionOne:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        3888 ms	16.7 MB
        :param lists:
        :return:
        """
        res = ListNode(0)
        p = res
        first_nodes = []
        for i in range(len(lists)):
            if lists[i]:
                first_nodes.append(lists[i])

        while len(first_nodes) > 1:
            min_index = get_min_node(first_nodes)
            q = first_nodes[min_index]
            if first_nodes[min_index].next is None:
                first_nodes.remove(first_nodes[min_index])
            else:
                first_nodes[min_index] = first_nodes[min_index].next
            p.next = q
            p = q
        if len(first_nodes) == 1:
            p.next = first_nodes[0]
        return res.next


class SolutionTwo:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        	68 ms	17.5 MB
        :param lists:
        :return:
        """
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        92 ms	16.7 MB
        :param lists:
        :return:
        """
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


class Test(unittest.TestCase):
    def test_one(self):
        inputs = ["[1,4,5]",
                  "[1,3,4]",
                  "[2,6]"]

        heads = [stringToListNode(s) for s in inputs]
        for head in heads:
            prettyPrintLinkedList(head)
        result = Solution().mergeKLists(heads)
        prettyPrintLinkedList(result)
