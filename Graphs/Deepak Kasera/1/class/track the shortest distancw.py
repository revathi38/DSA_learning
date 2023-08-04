"""
Track the path from destintion to sorce in a graph
"""

from collections import defaultdict, deque


def solve(nodes, edges, src, dest):
    # craete a adjacency list(graph)
    n = len(nodes)
    graph = defaultdict(list)
    for i in range(len(edges)):
        graph[nodes[i]].append(edges[i])
        graph[edges[i]].append(nodes[i])

    visited = [False] * (n + 1)
    parents = [-1] * (n + 1)
    q = deque()
    q.append(src)
    visited[src] = True

    while q:
        curr_node = q.popleft()

        for j in range(len(graph[curr_node])):
            sub_list_node = graph[curr_node][j]
            if not visited[sub_list_node]:
                parents[sub_list_node] = curr_node
                q.append(sub_list_node)
                visited[sub_list_node] = True

    track_path = []
    d = dest

    while d != -1:
        track_path.append(d)
        d = parents[d]

    return track_path


print(solve([1, 1, 2, 2, 4, 3, 3], [2, 4, 4, 3, 5, 5, 6], 1, 6))
# TC: O(E)
# SC: O(E) +O(N)
