from collections import defaultdict

class Solution:
    def makeEqual(self, words) -> bool:
        dictionary = defaultdict(int)
        for word in words:
            for letter in word:
                dictionary[letter] += 1

        for key in dictionary:
            if dictionary[key] % len(words) != 0:
                return False
        return True
    