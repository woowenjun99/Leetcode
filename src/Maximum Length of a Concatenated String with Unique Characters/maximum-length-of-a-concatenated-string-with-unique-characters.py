"""
Topic: Backtracking

We try out every possible permutations and get the maximum length
of each permutation.
"""
from typing import List

class Solution:
    def __init__(self) -> None:
        self.result = 0

    def maxLength(self, arr: List[str]) -> int:
        # Remove the elements with duplicated letter.
        arr = [x for x in arr if len(set(x)) == len(x)]

        def backtracking(index: int, used: set):
            if index == len(arr) or len(used) == 26: return

            for i in range(index, len(arr)):
                letters_in_arri = set(arr[i])
                if letters_in_arri.intersection(used): continue
                copied = used.union(letters_in_arri)
                self.result = max(self.result, len(copied))
                backtracking(i, copied)

        backtracking(0, set())

        return self.result