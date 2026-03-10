
def manhattan(pos, goal):
    # Heuristic: Manhattan distance from pos to goal
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

def best_first_search(maze, start, goal):
    """Find a path from start to goal using Greedy Best-First Search (list-based frontier)."""
    rows, cols = len(maze), len(maze[0])

    frontier = [(start, manhattan(start, goal))]  # List-based priority queue (sorted manually)
    visited = set()                                # Track visited positions
    came_from = {start: None}                      # Path reconstruction

    while frontier:
        # Sort frontier manually by heuristic value (ascending)
        frontier.sort(key=lambda x: x[1])
        current_pos, _ = frontier.pop(0)           # Get position with best heuristic

        if current_pos in visited:
            continue

        visited.add(current_pos)

        # If goal is reached, reconstruct path
        if current_pos == goal:
            path = []
            while current_pos is not None:
                path.append(current_pos)
                current_pos = came_from[current_pos]
            path.reverse()
            return path

        # Expand neighbors (up, down, left, right)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited):
                came_from[new_pos] = current_pos
                frontier.append((new_pos, manhattan(new_pos, goal)))

    return None  # No path found

def get_permutations(items):
    """Generate all orderings of a list without using any library."""
    if len(items) <= 1:
        return [list(items)]
    result = []
    for i in range(len(items)):
        rest = items[:i] + items[i+1:]
        for perm in get_permutations(rest):
            result.append([items[i]] + perm)
    return result

def find_multi_goal_path(maze, start, goals):
    """
    Find the SHORTEST path from start visiting ALL goal points.
    Tries every possible ordering of goals and keeps the one
    with the fewest total steps.
    """
    best_path = None
    best_length = float('inf')
    best_order = None

    for goal_order in get_permutations(list(goals)):
        current_pos = start
        total_path = []
        valid = True

        for goal in goal_order:
            segment = best_first_search(maze, current_pos, goal)
            if segment is None:
                valid = False
                break
            # Skip first node of each segment to avoid duplicating the junction
            total_path.extend(segment if not total_path else segment[1:])
            current_pos = goal

        if valid and len(total_path) < best_length:
            best_length = len(total_path)
            best_path = total_path
            best_order = goal_order

    if best_path:
        print(f"Optimal goal visit order: {best_order}")
    return best_path

def visualize_maze(maze, path, start, goals):
    """Print the maze with the path, start, and goals marked."""
    visual = [['#' if cell == 1 else '.' for cell in row] for row in maze]
    for r, c in path:
        visual[r][c] = '*'
    visual[start[0]][start[1]] = 'S'
    for i, (r, c) in enumerate(goals):
        visual[r][c] = str(i + 1)  # Label each goal with its number
    print("\nMaze (S=start, 1/2/3=goals, *=path, #=wall, .=open):")
    for row in visual:
        print(' '.join(row))

# -------------------------------------------------------------------
# Maze: 0 = open cell, 1 = wall
# Features several dead ends and three goal points at varied locations
# -------------------------------------------------------------------
maze = [
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

start = (0, 0)
goals = [(0, 5), (5, 0), (5, 5)]  # Three goal points spread across the maze

print("=== Enhanced Maze Navigation with Multiple Goals ===")
print(f"Start : {start}")
print(f"Goals : {goals}\n")

path = find_multi_goal_path(maze, start, goals)
if path:
    print(f"Path visiting all goals: {path}")
    print(f"Total steps: {len(path) - 1}")
    visualize_maze(maze, path, start, goals)
else:
    print("No path found that visits all goals")