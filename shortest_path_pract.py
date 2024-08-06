def shortest_path(edges, n, src):

    # convert the edges into adjacency list
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    # dist array with inf values
    dist = [float('inf')] * n
    dist[src] = 0
    q = [src]

    while q:
        node = q.pop(0)

        for neighbours in adj[node]:
            if dist[node] + 1 < dist[neighbours]:
                dist[neighbours] = dist[node] + 1
                # q.append(neighbours)

    return dist

    # answer_array = [-1]*n
    # for i in range(n):
    #     if dist[i] != float('inf'):
    #         answer_array[i] = dist[i]

    # return answer_array


n = 9
edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6],
         [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]
src = 0

ans = shortest_path(edges, n, src)
print(ans)
