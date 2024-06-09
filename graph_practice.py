def findCircleNum(isConnected):

    n = len(isConnected)
    visited = [False]*n
    provinces_ct = 0

    def dfs(city):
        for adjacent_city in range(n):
            if isConnected[city][adjacent_city] == 1 and visited[adjacent_city] is False:
                visited[adjacent_city] = True
                dfs(adjacent_city)

    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces_ct += 1

    return provinces_ct


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(findCircleNum(isConnected))
