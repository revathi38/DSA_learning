"""
Given an undirected graph source node
destination node Check if the destination node
can be visited from source node
"""
from collections import defaultdict, deque


def solve(nodes, edges, src, dest):
    # create adjancey list
    n = len(nodes)
    graph = defaultdict(list)
    for i in range(len(edges)):
        graph[nodes[i]].append(edges[i])
        graph[edges[i]].append(nodes[i])

    visited = [False] * (n + 1)
    q = deque()

    q.append(src)
    visited[src] = True

    while q:
        current_node = q.popleft()

        for j in range(len(graph[current_node])):
            if visited[graph[current_node][j]] == False:
                visited[graph[current_node][j]] = True
                q.append(graph[current_node][j])

    return visited[dest]


print(solve([1, 1, 2, 2, 4, 3, 3], [2, 4, 4, 3, 5, 5, 6], 1, 6))
# TC: O(E)
# SC: O(E) +O(N)
