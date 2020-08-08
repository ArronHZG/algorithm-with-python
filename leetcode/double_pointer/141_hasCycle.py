import unittest

from utils import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if not head:
            return False

        fast = slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True

        return False
