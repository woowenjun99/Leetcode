class Solution:
    def minOperations(self, s: str) -> int:
        combination_one = True
        combination_two = False

        score_of_one = score_of_two = 0
        for i in range(len(s)):
            isOne = s[i] == "1"
            if combination_one != isOne:
                score_of_one += 1
            if combination_two != isOne:
                score_of_two += 1
            combination_one = not combination_one
            combination_two = not combination_two
    
        return min(score_of_one, score_of_two)