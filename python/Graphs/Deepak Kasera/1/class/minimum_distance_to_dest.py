"""
Minimum distance from source to destination
"""

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
    

    visited = [False] * (n+1)
    level = [None] * (n+1) # initialize size

    q = deque()

    q.append(src)
    visited[src] = True
    level[src] = 0  # src node initial level 

    while q:
        current_node = q.popleft()

        for j in range(len(graph[current_node])):
            sub_node = graph[current_node][j]
            if visited[sub_node] == False:
                level[sub_node] = level[current_node] + 1  # increment to parent node
                visited[sub_node] = True
                q.append(sub_node)
    
    return level[dest]


print(solve([1, 1, 2, 2, 4, 3, 3], [2, 4, 4, 3, 5, 5, 6], 1, 6))
#TC: O(E)
#SC: O(E) +O(N)