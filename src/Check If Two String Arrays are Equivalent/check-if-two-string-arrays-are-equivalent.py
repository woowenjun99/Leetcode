from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        left_index = right_index = 0
        left = right = 0

        while left_index < len(word1) and right_index < len(word2) and word1[left_index][left] == word2[right_index][right]:
            left = left + 1 if left + 1 < len(word1[left_index]) else 0
            right = right + 1 if right + 1 < len(word2[right_index]) else 0
            left_index = left_index + 1 if left == 0 else left_index
            right_index = right_index + 1 if right == 0 else right_index
        
        return left_index == len(word1) and right_index == len(word2)