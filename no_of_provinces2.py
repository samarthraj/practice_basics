def findCircleNum(isConnected):
    n = len(isConnected) 
    province_no = 0
    visited = [False] * n 

    def dfs(city): 
        for adjacent_city in range(n): 
            if isConnected[city][adjacent_city] == 1 and visited[adjacent_city] is False: 
                visited[adjacent_city] = True
                dfs(adjacent_city)

    for city in range(n): 
        if not visited[city]: 
            dfs(city)
            province_no += 1
    
    return province_no

# Example usage:
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
# isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(findCircleNum(isConnected))  # Output: 2