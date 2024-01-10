from typing import Optional
from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Use DFS to create an undirected graph
        graph = defaultdict(list)
        def dfs(source: Optional[TreeNode]):
            if not source: return
            if source.left:
                graph[source.val].append(source.left.val)
                graph[source.left.val].append(source.val)
                dfs(source.left)
            if source.right:
                graph[source.val].append(source.right.val)
                graph[source.right.val].append(source.val)
                dfs(source.right)

        dfs(root)

        # Start BFS
        time = 0
        visited = set([start])
        queue = deque([[start, 0]])
        while queue:
            node, time_node_was_infected = queue.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append([neighbour, time_node_was_infected + 1])
                    time = max(time_node_was_infected + 1, time)
        
        return time