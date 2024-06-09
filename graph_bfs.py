from typing import List


class Solution:
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # List to store the BFS traversal order
        bfs_order = []
        # Set to keep track of visited nodes
        visited = set()
        # Queue for BFS
        queue = []

        # We will start BFS from the first vertex (0)
        start_node = 0
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            #Dequeue a vertex from the front of the queue
            vertex = queue.pop(0)
            # Process the node (here we simply append it to the traversal list)
            bfs_order.append(vertex)

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it visited and enqueue it
            for neighbor in adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_order


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
    traversal = sol.bfsOfGraph(V, adj)
    print(f"BFS traversal of the graph: {traversal}")
