class Solution:
    def maxScore(self, s: str) -> int:
        left = 0 if s[0] == "1" else 1
        right = s[1:].count("1")
        max_score_so_far = left + right

        for i in range(1, len(s) - 1):
            left = left + 1 if s[i] == "0" else left
            right = right - 1 if s[i] == "1" else right
            max_score_so_far = max(max_score_so_far, left + right)

        return max_score_so_far