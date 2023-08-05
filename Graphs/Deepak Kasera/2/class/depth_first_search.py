from collections import defaultdict

def dfs(graph, visited, s):
    if visited[s]:
        return
    
    visited[s] = True
    for i in range(len(graph[s])):
        v = graph[s][i]
        dfs(graph, visited, v)

def solve(edges, nodes, src, dest):
    adjacency_list = defaultdict(list)
    visited = [False] * (len(nodes) + 1)

    for u, v in edges:
        adjacency_list[u].append(v)
    
    dfs(adjacency_list, visited, src)
    return visited[dest]



print(solve([(1, 2), (1, 9), (2, 1), (2, 15), (2, 3), (3, 2), (3, 7), (3, 8), (3, 4), (4, 3), (4, 5), (5, 6), (5, 11), (5, 4), (6, 5), (7, 3), (8, 3), (9, 1), (10, 15), (11, 5), (11, 12), (11, 13), (12, 11), (13, 11), (13, 14), (14, 13), (15, 10), (15, 2)], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 5, 14))