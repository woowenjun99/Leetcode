"""
(1). If the two strings have 2 different lengths, there is no way they can be 
the same if you do the 2 operations, so we can reduce False immediately.

(2). If there exists a letter in word1 that does not exist in word2, we can no 
longer achieve the same string with both operations. (e.g. word1 = "c" and 
word2 = "d")

(3). This point is harder than I thought of. I realised no matter what you 
do the occurrences are still the same, whether you swap the letters around 
or swap the occurrence with another. It is like a cycle per se, no matter 
what you do it is still the same (e.g. Tower of Hanoi or Cycle sort). 
Just match the occurrences can already
"""
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:        
        counter_one = Counter(word1)
        counter_two = Counter(word2)

        return len(word1) == len(word2) and set(counter_one.keys()) == set(counter_two.keys()) and sorted(counter_one.values()) == sorted(counter_two.values())