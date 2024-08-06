class Solution:
    def orangesRotting(self, grid):
        queue = []
        n = len(grid)
        m = len(grid[0])
        visited_array = [[0] * m for i in range(n)]

        r_delta = [-1, 0, 1, 0]
        c_delta = [0, 1, 0, -1]
        tm = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited_array[r][c] = 2

        while queue:
            for _ in range(len(queue)):
                r, c, t = queue.pop(0)
                tm = max(t, tm)

                for i in range(4):
                    new_row = r + r_delta[i]
                    new_col = c + c_delta[i]

                    if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1 and visited_array[new_row][new_col] != 2:
                        visited_array[new_row][new_col] = 2
                        queue.append((new_row, new_col, tm + 1))
        return tm


# Example usage:
grid1 = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
grid2 = [[0, 2]]

ro = Solution()
# Expected output: [[2, 2, 2], [2, 2, 0], [0, 2, 1]]
# print(ro.orangesRotting(grid1))
# print(ro.orangesRotting(grid2))  # Expected output: [[0, 2]]
