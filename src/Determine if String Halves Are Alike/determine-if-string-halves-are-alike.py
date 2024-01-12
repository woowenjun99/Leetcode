class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = num_of_vowels_on_left = num_of_vowels_on_right = 0
        right = len(s) // 2

        while left < len(s) // 2 and right < len(s):
            left_lower = s[left].lower()
            right_lower = s[right].lower()
            num_of_vowels_on_left += 1 if (left_lower == "a" or left_lower == "e" or left_lower == "i" or left_lower == "o" or left_lower == "u") else 0
            num_of_vowels_on_right += 1 if (right_lower == "a" or right_lower == "e" or right_lower == "i" or right_lower == "o" or right_lower == "u") else 0
            left += 1
            right += 1

        return num_of_vowels_on_right == num_of_vowels_on_left