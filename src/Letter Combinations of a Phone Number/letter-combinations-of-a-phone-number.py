from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        response = []

        def dfs(digits: str, built: str, index: int):
            if len(built) == len(digits) and built:
                response.append(built)
                return
            
            for i in range(index, len(digits)):
                for j in combinations[digits[i]]:
                    dfs(digits, built + j, i + 1)

        dfs(digits, "", 0)

        return response