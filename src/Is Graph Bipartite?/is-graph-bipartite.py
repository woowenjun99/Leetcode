from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colours = [-1] * len(graph)
        q = deque()
        for i in range(len(graph)):
            # If not yet coloured, assign an arbitrary colour.
            if colours[i] == -1:
                colours[i] = 0
                q.append([i, 0])
                while q:
                    front = q.pop()
                    for neighbour in graph[front[0]]:
                        # If neighbour colour same as parent
                        if colours[neighbour] == front[1]:
                            return False
                        if colours[neighbour] == -1:
                            colours[neighbour] = 1 if front[1] == 0 else 0
                            q.append([neighbour, colours[neighbour]])
        return True