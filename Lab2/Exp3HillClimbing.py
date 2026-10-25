
"""
Experiment 3: Hill Climbing Algorithm
AI Lab - IC-709D

Find a goal state using heuristic-based search.
"""


def hill_climbing(graph, heuristic, start, goal):
    """Perform Steepest-Ascent Hill Climbing."""

    current = start
    path = [current]
    visited = {current}

    print("\nStarting Hill Climbing Search...")
    print("-" * 45)

    while current != goal:

        print(f"\nCurrent Node: {current}")
        print(f"Heuristic Value: {heuristic[current]}")

        neighbors = graph.get(current, [])

        # Select the best unvisited neighbor
        available_neighbors = [
            node for node in neighbors
            if node not in visited
        ]

        if not available_neighbors:
            print("\nNo unexplored neighboring states available.")
            print("Search stopped.")
            return path, False

        best_neighbor = max(
            available_neighbors,
            key=lambda node: heuristic[node]
        )

        print("Evaluating Neighbors:")

        for neighbor in available_neighbors:
            print(
                f"  {neighbor}: "
                f"Heuristic = {heuristic[neighbor]}"
            )

        # Move only if the neighbor is better
        if heuristic[best_neighbor] <= heuristic[current]:

            print("\nNo better neighboring state found.")
            print("Algorithm is stuck at a local maximum.")

            return path, False

        current = best_neighbor
        visited.add(current)
        path.append(current)

        print(f"Moving to: {current}")

    print("\nGoal State Reached!")

    return path, True


def main():
    """Main function."""

    # Graph representation
    graph = {
        "S": ["A", "B"],
        "A": ["C", "D"],
        "B": [],
        "C": ["G"],
        "D": [],
        "G": []
    }

    # Heuristic values (higher is better)
    heuristic = {
        "S": 1,
        "A": 4,
        "B": 2,
        "C": 6,
        "D": 5,
        "G": 10
    }

    print("=" * 50)
    print("          HILL CLIMBING ALGORITHM")
    print("=" * 50)

    start = input("\nEnter starting node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("\nInvalid node! Available nodes: S, A, B, C, D, G")
        return

    path, success = hill_climbing(
        graph,
        heuristic,
        start,
        goal
    )

    print("\n" + "=" * 50)
    print("                FINAL RESULT")
    print("=" * 50)

    print("Path:", " -> ".join(path))
    print("Number of Moves:", len(path) - 1)

    if success:
        print("Status: Goal successfully reached.")
    else:
        print("Status: Goal not reached.")


if __name__ == "__main__":
    main()
