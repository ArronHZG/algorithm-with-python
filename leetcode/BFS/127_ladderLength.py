import unittest
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0
        if beginWord in word_set:
            word_set.remove(beginWord)
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        step = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                word_list = list(word)
                for j in range(len(beginWord)):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0


class Test(unittest.TestCase):
    def test_one(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        answer = 5

        result = Solution().ladderLength(beginWord, endWord, wordList)
        self.assertEqual(answer, result)
