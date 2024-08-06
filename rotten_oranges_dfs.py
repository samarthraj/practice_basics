class Solution:
    def dfs(self, grid, time, initial_row, initial_col, new_grid, delta_row, delta_col):
        new_grid[initial_row][initial_col] = 2
        time[0] = time[0] + 0.15
        n = len(grid)
        m = len(grid[0])

        for i in range(4):
            new_row = initial_row + delta_row[i]
            new_col = initial_col + delta_col[i]

            if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1 and new_grid[new_row][new_col] != 2:
                self.dfs(grid, time, new_row, new_col,
                         new_grid, delta_row, delta_col)

    def orangesRotting(self, grid):
        # have to find the rotten orange
        time = [0]
        initial_row = 0
        initial_col = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    initial_row = r
                    initial_col = c

        new_grid = [row[:] for row in grid]

        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]

        self.dfs(grid, time, initial_row, initial_col,
                new_grid, delta_row, delta_col)
        return time[0]


ro = Solution()
# Example usage:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
grid2 = [[0,2]]
print(ro.orangesRotting(grid))  # Output: 4
