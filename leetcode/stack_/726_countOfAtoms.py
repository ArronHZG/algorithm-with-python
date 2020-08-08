import unittest
from collections import Counter
from typing import List


def get_atom(N, formula, i):
    start = i
    i += 1
    while i < N and formula[i].islower():
        i += 1
    atom = formula[start:i]
    return i, atom


def get_multiplicity(N, formula, i):
    start = i
    while i < N and formula[i].isdigit():
        i += 1
    multiplicity = int(formula[start:i] or 1)
    return i, multiplicity


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        遇到(), 单独统计()中原子的数量
        :param formula:
        :return:
        """
        i, N = 0, len(formula)
        stack = [Counter()]
        while i < N:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i, m = get_multiplicity(N, formula, i + 1)
                for atom, value in top.items():
                    stack[-1][atom] += value * m
            else:
                i, atom = get_atom(N, formula, i)
                i, m = get_multiplicity(N, formula, i)
                stack[-1][atom] += m
        top = stack.pop()
        return "".join(atom + (str(top[atom]) if top[atom] > 1 else '') for atom in sorted(top))


class Test(unittest.TestCase):
    def test_one(self):
        formula = "Mg(OH)2"
        answer = "H2MgO2"
        result = Solution().countOfAtoms(formula)
        self.assertEqual(answer, result)
