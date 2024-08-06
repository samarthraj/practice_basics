# first of all we will have to do only bfs, dfs in this will not give us minimum time
class Solution:
    def orangesRotting(self, grid):
        queue = []
        n = len(grid)
        m = len(grid[0])
        visited_array = [[0] * m for r in range(n)]

        del_r = [-1, 0, 1, 0]
        del_c = [0, 1, 0, -1]

        # find the rotten oranges first
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # the last one is time
                    visited_array[r][c] = 2
                else:
                    visited_array[r][c] = grid[r][c]

        time = 0
        while queue:
            for _ in range(len(queue)):
                r, c, t = queue.pop(0)
                time = max(t, time)

                for i in range(4):
                    new_r = r + del_r[i]
                    new_c = c + del_c[i]
                    if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1 and visited_array[new_r][new_c] != 2:
                        visited_array[new_r][new_c] = 2
                        queue.append((new_r, new_c, time + 1))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited_array[r][c] == 1:
                    return -1
        return time


# Example usage:
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
grid2 = [[0, 2]]

grid3 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

ro = Solution()
# Expected output: [[2, 2, 2], [2, 2, 0], [0, 2, 1]]
# print(ro.orangesRotting(grid1))
# print(ro.orangesRotting(grid2))  # Expected output: [[0, 2]]
print(ro.orangesRotting(grid3))
