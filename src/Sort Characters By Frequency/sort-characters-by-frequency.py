from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        key_value_pairs = sorted([(counter[key], key) for key in counter], reverse=True)
        new_str = ""
        for occurrence, letter in key_value_pairs: new_str += letter * occurrence
        return new_str