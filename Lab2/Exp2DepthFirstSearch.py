
"""
Experiment 2: Depth First Search (DFS)
AI Lab - IC-709D

Graph traversal and path finding using DFS.
"""


def dfs(graph, start, goal):
    """Perform iterative DFS and find a path."""

    stack = [(start, [start])]
    visited = set()
    traversal_order = []

    while stack:

        current_node, path = stack.pop()

        if current_node in visited:
            continue

        visited.add(current_node)
        traversal_order.append(current_node)

        # Check whether the goal is reached
        if current_node == goal:
            return traversal_order, path

        # Add neighbors in reverse order
        neighbors = graph.get(current_node, [])

        for neighbor in reversed(neighbors):

            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

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
    print("       DEPTH FIRST SEARCH (DFS)")
    print("=" * 45)

    start = input("Enter starting node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("Invalid node! Available nodes are A, B, C, D, E, F, G.")
        return

    traversal, path = dfs(graph, start, goal)

    print("\nDFS Traversal:")
    print(" -> ".join(traversal))

    if path:
        print("\nPath Found:")
        print(" -> ".join(path))
        print("Path Length:", len(path) - 1)

    else:
        print("\nGoal node is not reachable.")


if __name__ == "__main__":
    main()
