"""
Topic: Hashmap

If the same letter appear in both string, we can remove the matched
pairs, meaning we match one letter in s to the one of the
same letter in t. 

Essentially, we are trying to find the number of 'swaps' to make
the strings anagram. If we swap a letter in s to a letter in t,
we can remove both. The answer is just the total letters remaining that
needs to be swapped in s.
"""
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = dict(Counter(s))
        counter_t = dict(Counter(t))
        number_of_swaps = 0

        for letter in counter_s:
            if letter in counter_t:
                if counter_s[letter] <= counter_t[letter]: continue
                number_of_swaps += counter_s[letter] - counter_t[letter]
            else: 
                number_of_swaps += counter_s[letter]

        return number_of_swaps