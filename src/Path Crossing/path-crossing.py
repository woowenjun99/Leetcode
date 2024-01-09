from collections import defaultdict

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = defaultdict(set)
        x = y = 0
        visited[x].add(y)
        for letter in path:
            if letter == "N":
                y += 1
            elif letter == "S":
                y -= 1
            elif letter == "W":
                x -= 1
            else:
                x += 1
            
            if y in visited[x]:
                return True
            visited[x].add(y)
        
        return False