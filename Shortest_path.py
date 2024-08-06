class Solution:
    def shortestPath(self, edges, n, src):
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        # creating an array with infinite values
        dist = [float('inf')] * n
        dist[src] = 0
        q = [src]

        while q:
            node = q.pop(0)
            for neighbour in adj[node]:
                if dist[node] + 1 < dist[neighbour]:
                    dist[neighbour] = dist[node] + 1
                    q.append(neighbour)

        ans = [-1] * n
        for i in range(n):
            if dist[i] != float('inf'):
                ans[i] = dist[i]

        return ans


n = 9
edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6],
         [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]
src = 0
solution = Solution()
ans = solution.shortestPath(edges, n, src)
print(ans)
