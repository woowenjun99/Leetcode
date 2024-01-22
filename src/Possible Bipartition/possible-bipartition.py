from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        colours = [-1] * (n + 1)
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        for i in range(1, n + 1):
            if colours[i] == -1:
                colours[i] = 0
                queue = deque([[i, 0]])
                while queue:
                    parent, colour = queue.popleft()
                    for neighbour in graph[parent]:
                        if colours[neighbour] == colour:
                            return False
                        if colours[neighbour] == -1:
                            colours[neighbour] = 1 - colour
                            queue.append([neighbour, colours[neighbour]])
        return True