def findCircleNum(isConnected):
    def dfs(city):
        for adjacent_city in range(n):
            if isConnected[city][adjacent_city] == 1 and not visited[adjacent_city]:
                visited[adjacent_city] = True
                dfs(adjacent_city)

    n = len(isConnected)
    visited = [False] * n
    provinces = 0

    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces += 1

    return provinces


# Example usage:
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
#isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))  # Output: 2
