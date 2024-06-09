from typing import List


class Solution:
    def dfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # List to store the DFS traversal order
        dfs_order = []
        # Set to keep track of visited nodes
        visited = set()
        # Stack for DFS
        stack = []

        # We will start DFS from the first vertex (0)
        start_node = 0
        stack.append(start_node)

        while stack:
            # Pop a vertex from the stack
            vertex = stack.pop()
            if vertex not in visited:
                # Process the node (here we simply append it to the traversal list)
                dfs_order.append(vertex)
                visited.add(vertex)

                # Push all adjacent vertices of the popped vertex into the stack
                # We need to add in reverse order to maintain the correct DFS order
                for neighbor in reversed(adj[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return dfs_order


# Example usage
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    V = 6
    adj = [
        [1, 2],    # Neighbors of vertex 0
        [0, 3, 4],  # Neighbors of vertex 1
        [0, 5],    # Neighbors of vertex 2
        [1],       # Neighbors of vertex 3
        [1, 5],    # Neighbors of vertex 4
        [2, 4]     # Neighbors of vertex 5
    ]

    sol = Solution()
    traversal = sol.dfsOfGraph(V, adj)
    print(f"DFS traversal of the graph: {traversal}")
