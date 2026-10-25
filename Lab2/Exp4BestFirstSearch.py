
"""
Experiment 4: Greedy Best First Search
AI Lab - IC-709D

Find a path using heuristic-based priority search.
"""

import heapq
from itertools import count


def best_first_search(graph, heuristic, start, goal):
    """Perform Greedy Best First Search."""

    priority_queue = []
    counter = count()

    # Store: (heuristic, insertion order, current node, path)
    heapq.heappush(
        priority_queue,
        (heuristic[start], next(counter), start, [start])
    )

    visited = set()
    traversal_order = []

    while priority_queue:

        h_value, _, current, path = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)
        traversal_order.append(current)

        print(
            f"Exploring Node: {current} "
            f"(Heuristic: {h_value})"
        )

        # Check goal state
        if current == goal:
            return traversal_order, path

        # Explore neighboring nodes
        for neighbor in graph.get(current, []):

            if neighbor not in visited:

                new_path = path + [neighbor]

                heapq.heappush(
                    priority_queue,
                    (
                        heuristic[neighbor],
                        next(counter),
                        neighbor,
                        new_path
                    )
                )

    return traversal_order, None


def main():
    """Main function."""

    graph = {
        "S": ["A", "B"],
        "A": ["C", "D"],
        "B": ["E", "F"],
        "C": [],
        "D": [],
        "E": ["G"],
        "F": [],
        "G": []
    }

    # Estimated distance to the goal
    heuristic = {
        "S": 7,
        "A": 6,
        "B": 4,
        "C": 5,
        "D": 7,
        "E": 2,
        "F": 5,
        "G": 0
    }

    print("=" * 50)
    print("       GREEDY BEST FIRST SEARCH")
    print("=" * 50)

    start = input("\nEnter starting node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("Invalid node! Available nodes: S, A, B, C, D, E, F, G")
        return

    print("\nSearch Process:")
    print("-" * 50)

    traversal, path = best_first_search(
        graph,
        heuristic,
        start,
        goal
    )

    print("\n" + "=" * 50)
    print("                FINAL RESULT")
    print("=" * 50)

    print("Traversal Order:", " -> ".join(traversal))

    if path:
        print("Path Found:", " -> ".join(path))
        print("Path Length:", len(path) - 1)

    else:
        print("Goal node is not reachable.")


if __name__ == "__main__":
    main()
