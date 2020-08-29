import unittest


class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)  # 以空格为分隔符，分隔成两个
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key=f)


class Test(unittest.TestCase):
    def test_one(self):
        input = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        answer = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]

        result = Solution().reorderLogFiles(input)
        self.assertEqual(answer, result)
