from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        alphabets = [0] * 26
        for c in count:
            alphabets[ord(c) - ord('a')] = count[c]

        score = 0
        for word in words:
            can_be_formed = True
            count = Counter(word)
            for c in count:
                if alphabets[ord(c) - ord('a')] < count[c]:
                    can_be_formed = False
                    break
            score = len(word) + score if can_be_formed else score

        return score