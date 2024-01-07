from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, required in prerequisites: graph[required].append(course)
        incoming_edges = [0] * numCourses
        for src in graph:
            for dest in graph[src]:
                incoming_edges[dest] += 1
        q = deque()
        times_processed = 0

        # Add in the nodes that have indegree of 0.
        for index, incoming_edge in enumerate(incoming_edges):
            if not incoming_edge:
                q.append(index)

        while q:
            front = q.popleft()
            times_processed += 1
            for dest in graph[front]:
                incoming_edges[dest] -= 1
                if not incoming_edges[dest]: 
                    q.append(dest)
              
        return times_processed == numCourses