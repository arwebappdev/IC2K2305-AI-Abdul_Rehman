
"""
Experiment 2: Water Jug Problem using BFS
AI Lab - IC-709D

Jug A capacity: 4 litres
Jug B capacity: 3 litres
Target: 2 litres
"""

from collections import deque


def get_next_states(state):
    """Generate all possible states from the current state."""

    a, b = state

    next_states = [
        ((4, b), "Fill Jug A"),
        ((a, 3), "Fill Jug B"),
        ((0, b), "Empty Jug A"),
        ((a, 0), "Empty Jug B"),
        (
            (a - min(a, 3 - b), b + min(a, 3 - b)),
            "Pour Jug A into Jug B"
        ),
        (
            (a + min(b, 4 - a), b - min(b, 4 - a)),
            "Pour Jug B into Jug A"
        )
    ]

    return next_states


def water_jug_bfs():
    """Solve the Water Jug Problem using BFS."""

    initial_state = (0, 0)
    target = 2

    queue = deque([(initial_state, [])])
    visited = {initial_state}

    while queue:
        current_state, path = queue.popleft()

        a, b = current_state

        if a == target or b == target:
            return path + [(current_state, "Goal Reached")]

        for next_state, action in get_next_states(current_state):

            if next_state not in visited:
                visited.add(next_state)

                new_path = path + [(current_state, action)]

                queue.append((next_state, new_path))

    return None


def main():
    print("=" * 45)
    print("       WATER JUG PROBLEM - BFS")
    print("=" * 45)

    solution = water_jug_bfs()

    if solution:
        print("\nSolution Found!\n")

        for step, (state, action) in enumerate(solution):
            print(f"Step {step}: State {state} -> {action}")

        print("\nGoal: Exactly 2 litres of water obtained.")

    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
