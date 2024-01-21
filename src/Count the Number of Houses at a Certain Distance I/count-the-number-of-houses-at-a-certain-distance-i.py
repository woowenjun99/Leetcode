from typing import List
from collections import defaultdict, deque

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
            graph[i + 1].append(i)
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

        results = [0] * (n + 1)
        for i in range(n):
            queue = deque([[i, 0]])
            visited = [False] * n
            visited[i] = True
            while queue:
                parent, distance = queue.popleft()
                for neighbour in graph[parent]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        results[distance + 1] += 1
                        queue.append([neighbour, distance + 1])

        return results[1:]