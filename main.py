"""
Topic: Sorting

(1). We need to realise that we are keying does not matter.
What matters is the occurrence of the letter.

(2). Supposed that a letter appears multiple times than
another, we would want to push as little times as possible.
Therefore, we need to prioritise the letters that appears 
most time. We can do so using a priority queue or sorting.

Space Complexity: O(1) because we know that PQ will at most 
26 elements as there are 26 letters in the alphabet.

Time Complexity: O(n) where n is the length of word because
we need to count the occurrence of each letter.
"""
from collections import Counter
from heapq import heappop, heapify

class Solution:
    def minimumPushes(self, word: str) -> int:
        pq = []
        counter = Counter(word)
        for key in counter: pq.append(-counter[key])
        heapify(pq)
        
        result = counter = 0
        letters = 1
        while pq:
            occurrence  = heappop(pq)
            result -= letters * occurrence
            counter += 1
            if counter == 8:
                counter = 0
                letters += 1

        return result