def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = []
    visited = [[False] * cols for _ in range(rows)]

    # Initialize the queue with all rotten oranges and the time they start at 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
                visited[r][c] = True

    # Directions for 4-directional movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS to rot adjacent fresh oranges
    time_elapsed = 0
    while queue:
        # Dequeue an element from the front of the queue
        current_element = queue.pop()
        current_row = current_element[0]
        current_col = current_element[1]
        current_time = current_element[2]

        # Update the maximum time elapsed
        if current_time > time_elapsed:
            time_elapsed = current_time

        # Check all four possible directions
        for direction in directions:
            new_row = current_row + direction[0]
            new_col = current_col + direction[1]

            # Ensure the new cell is within grid bounds
            # if 0 <= new_row < rows and 0 <= new_col < cols:
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                # Check if the new cell contains a fresh orange and has not been visited
                if grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                    # Mark the orange as rotten
                    grid[new_row][new_col] = 2
                    # Mark the cell as visited
                    visited[new_row][new_col] = True
                    # Enqueue the new rotten orange with incremented time
                    queue.append((new_row, new_col, current_time + 1))

    # Check if there are any fresh oranges left
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return -1

    return time_elapsed


# Example usage:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(orangesRotting(grid))  # Output: 4
