
import heapq
import itertools
import time


GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


def manhattan_distance(state):
    """Calculate the total Manhattan distance of all numbered tiles."""
    distance = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        current_row, current_col = divmod(index, 3)
        goal_index = tile - 1
        goal_row, goal_col = divmod(goal_index, 3)

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def is_solvable(state):
    """A 3x3 puzzle is solvable when its inversion count is even."""
    tiles = [tile for tile in state if tile != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


def get_neighbors(state):
    """Generate all valid states by moving the blank tile."""
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)

    possible_moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    neighbors = []

    for row_change, col_change in possible_moves:
        new_row = row + row_change
        new_col = col + col_change

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank_index], new_state[new_index] = (
                new_state[new_index],
                new_state[blank_index]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def reconstruct_path(parent, state):
    """Reconstruct the path from the initial state to the goal."""
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    return path[::-1]


def a_star_search(start_state):
    """Solve the 8-Puzzle using A* Search."""
    counter = itertools.count()

    # Priority queue: (f_score, tie_breaker, g_score, state)
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (manhattan_distance(start_state), next(counter), 0, start_state)
    )

    parent = {start_state: None}
    g_score = {start_state: 0}

    nodes_expanded = 0

    while priority_queue:
        f_score, _, current_g, current_state = heapq.heappop(
            priority_queue
        )

        # Ignore outdated entries in the priority queue.
        if current_g != g_score.get(current_state):
            continue

        if current_state == GOAL_STATE:
            return (
                reconstruct_path(parent, current_state),
                nodes_expanded
            )

        nodes_expanded += 1

        for neighbor in get_neighbors(current_state):
            tentative_g = current_g + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                parent[neighbor] = current_state

                h_score = manhattan_distance(neighbor)
                new_f_score = tentative_g + h_score

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_score,
                        next(counter),
                        tentative_g,
                        neighbor
                    )
                )

    return None, nodes_expanded


def display_board(state):
    """Display a puzzle state as a 3x3 board."""
    for row in range(3):
        values = state[row * 3:(row + 1) * 3]
        print(" ".join("_" if tile == 0 else str(tile) for tile in values))
    print()


def main():
    print("===== 8-PUZZLE SOLVER USING A* SEARCH =====")
    print("Enter the initial board as 9 numbers (use 0 for blank).")
    print("Example: 2 8 3 1 6 4 7 0 5")

    try:
        values = list(map(int, input("Enter initial state: ").split()))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    if len(values) != 9 or set(values) != set(range(9)):
        print("Invalid board! Enter each number from 0 to 8 exactly once.")
        return

    start_state = tuple(values)

    if not is_solvable(start_state):
        print("This puzzle configuration is not solvable.")
        return

    print("\nInitial State:")
    display_board(start_state)

    start_time = time.perf_counter()

    solution_path, nodes_expanded = a_star_search(start_state)

    end_time = time.perf_counter()

    if solution_path is None:
        print("No solution found.")
        return

    print("===== SOLUTION =====")

    for step, state in enumerate(solution_path):
        print(f"Step {step}:")
        display_board(state)

    print("===== PERFORMANCE =====")
    print(f"Total moves: {len(solution_path) - 1}")
    print(f"Nodes expanded: {nodes_expanded}")
    print(f"Execution time: {(end_time - start_time):.6f} seconds")


if __name__ == "__main__":
    main()
