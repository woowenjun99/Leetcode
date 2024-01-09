from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        alphabets = defaultdict(list)
        for (index, letter) in enumerate(s): alphabets[letter].append(index)
        longest_distance = 0
        has_longest_distance = False
        for alphabet in alphabets:
            if len(alphabets[alphabet]) > 1: 
                longest_distance = max(longest_distance, alphabets[alphabet][-1] - alphabets[alphabet][0] - 1)
                has_longest_distance = True
        return longest_distance if has_longest_distance else -1