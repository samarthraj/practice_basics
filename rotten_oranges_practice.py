def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    visited = [[False] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # initial
                visited[r][c] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time_taken = 0
    while queue:
        current = queue.pop(0)
        current_row = current[0]
        current_col = current[1]
        current_time = current[2]

        for direction in directions:
            new_row = current_row + direction[0]
            new_col = current_col + direction[1]

            time_taken = max(time_taken, current_time)

            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                if grid[new_row][new_col] == 1 and visited[new_row][new_col] is False:
                    grid[new_row][new_col] = 2
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col, current_time + 1))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1

    return time_taken


# Example usage:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid))  # Output: 4
