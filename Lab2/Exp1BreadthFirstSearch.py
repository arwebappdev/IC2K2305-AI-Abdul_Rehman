
"""
Experiment 1: Breadth First Search (BFS)
AI Lab - IC-709D

Graph traversal and shortest path using BFS.
"""

from collections import deque


def bfs(graph, start, goal):
    """Perform BFS and find the shortest path."""

    queue = deque([[start]])
    visited = {start}
    traversal_order = []

    while queue:

        path = queue.popleft()
        current_node = path[-1]

        traversal_order.append(current_node)

        if current_node == goal:
            return traversal_order, path

        for neighbor in graph.get(current_node, []):

            if neighbor not in visited:

                visited.add(neighbor)

                new_path = path + [neighbor]
                queue.append(new_path)

    return traversal_order, None


def main():
    """Main function."""

    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [],
        "E": [],
        "F": [],
        "G": []
    }

    print("=" * 45)
    print("       BREADTH FIRST SEARCH (BFS)")
    print("=" * 45)

    start = input("Enter starting node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("Invalid node! Available nodes are A, B, C, D, E, F, G.")
        return

    traversal, path = bfs(graph, start, goal)

    print("\nBFS Traversal:")
    print(" -> ".join(traversal))

    if path:
        print("\nShortest Path:")
        print(" -> ".join(path))
        print("Path Length:", len(path) - 1)

    else:
        print("\nGoal node is not reachable.")


if __name__ == "__main__":
    main()
