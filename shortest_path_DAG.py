def topoSort(node, adj, visited, stack):
    visited[node] = True

    for neighbour, _ in adj[node]:
        if not visited[neighbour]:
            topoSort(neighbour, adj, visited, stack)
    stack.append(node)

def shortest_path_DAG(n, edges):

    adj = [[] for i in range(n)]

    for u, v, wt in edges:
        adj[u].append((v, wt))

    visited = [False] * n
    stack = []

    for i in range(n):
        if not visited[i]:
            topoSort(i, adj, visited, stack)

    dist = [float('inf')] * n
    src = 0
    dist[src] = 0

    while stack:
        node = stack.pop(0)
        if dist[node] != float('inf'):
            for neighbour, wt in adj[node]:
                if dist[node] + wt < dist[neighbour]:
                    dist[neighbour] = dist[node] + wt

    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1

    return dist


n = 9
edges = [
    [0, 1, 1], [0, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1],
    [1, 2, 1], [2, 6, 1], [6, 7, 1], [7, 8, 1], [6, 8, 1]
]
print(shortest_path_DAG(n, edges))