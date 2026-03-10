# Delivery graph: nodes are locations, edge costs are travel times (in minutes)
graph = {
    'Warehouse': {'D1': 5, 'D2': 8, 'D3': 12},
    'D1':        {'D2': 4, 'D4': 7},
    'D2':        {'D3': 3, 'D5': 6},
    'D3':        {'D5': 5, 'D6': 4},
    'D4':        {'D6': 8},
    'D5':        {'D6': 3},
    'D6':        {}
}

# Time windows: (open_time, deadline) in minutes from departure
time_windows = {
    'Warehouse': (0,  999),
    'D1':        (0,  20),   # Very strict
    'D2':        (5,  35),
    'D3':        (10, 40),
    'D4':        (0,  25),   # Strict
    'D5':        (15, 50),
    'D6':        (20, 60),   # Most flexible
}

# Heuristic for GBFS: use deadline — stricter deadline = lower value = visited first
heuristic = {node: tw[1] for node, tw in time_windows.items()}

# Greedy Best-First Search Function (without heapq)
def greedy_bfs(graph, start, goal):
    frontier = [(start, heuristic[start], 0)]  # (node, heuristic, arrival_time)
    visited = set()  # Set to keep track of visited nodes
    came_from = {start: None}  # Path reconstruction

    while frontier:
        # Sort frontier manually by heuristic value (ascending order)
        frontier.sort(key=lambda x: x[1])
        current_node, _, current_time = frontier.pop(0)  # Get node with best heuristic

        if current_node in visited:
            continue

        visited.add(current_node)

        # Check the time window when visiting each node
        open_t, deadline = time_windows[current_node]
        if current_time > deadline:
            status = f"LATE by {current_time - deadline} min!"
        elif current_time < open_t:
            status = f"Too early, wait {open_t - current_time} min"
        else:
            status = "On time"
        print(f"{current_node} (t={current_time} min) [{open_t}-{deadline}] -> {status}")

        # If goal is reached, reconstruct path
        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            print(f"Total travel time: {current_time} minutes")
            return

        # Expand neighbors: carry cumulative travel time
        for neighbor, travel_cost in graph[current_node].items():
            if neighbor not in visited:
                new_arrival = current_time + travel_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor], new_arrival))

    print("\nGoal not found")

# Run Greedy Best-First Search
print("\nFollowing is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'Warehouse', 'D6')

