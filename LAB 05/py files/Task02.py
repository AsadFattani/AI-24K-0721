

import random
import time

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}


def update_edge_costs(graph):
    """Randomly adjust every edge cost by ±2 (minimum 1). Returns only the changed edges."""
    changed = {}
    for node in graph:
        for neighbor in graph[node]:
            old = graph[node][neighbor]
            graph[node][neighbor] = max(1, old + random.randint(-2, 2))
            if graph[node][neighbor] != old:
                changed[(node, neighbor)] = (old, graph[node][neighbor])
    return changed


def propagate_cost_change(node, g_costs, came_from, visited, frontier, graph, heuristic):
    """
    Walk the came_from tree downstream from 'node' and push updated g-costs
    to every descendant, un-visiting and re-queuing each affected node.
    This avoids a full restart — only the invalidated sub-paths are reconsidered.
    """
    queue = [node]
    while queue:
        parent = queue.pop()
        for neighbor in graph.get(parent, {}):
            if came_from.get(neighbor) == parent:          # neighbor is on parent's path tree
                new_g = g_costs[parent] + graph[parent][neighbor]
                if new_g != g_costs.get(neighbor):
                    g_costs[neighbor] = new_g
                    visited.discard(neighbor)               # allow re-expansion
                    frontier.append((neighbor, new_g + heuristic[neighbor]))
                    queue.append(neighbor)                  # continue propagation downward


def dynamic_a_star(graph, start, goal, max_updates=3):
    """
    A* Search that adapts to dynamic edge cost changes without restarting from scratch.

    A single search loop runs to completion.  At random step intervals the edge
    costs are perturbed and the live search state (g_costs, frontier, visited,
    came_from) is surgically patched so that only the affected portions of the
    search are reconsidered.
    """
    print("\nFollowing is the Dynamic A* Search:\n")

    # Persistent search state — shared across all cost updates
    frontier  = [(start, heuristic[start])]
    visited   = set()
    g_costs   = {start: 0}
    came_from = {start: None}

    update_count   = 0
    step           = 0
    next_update_at = random.randint(2, 4)   # first update fires at a random step

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        step += 1
        print(f"Step {step}: Expanding '{current_node}'  "
              f"(g={g_costs[current_node]}, h={heuristic[current_node]}, f={current_f})")
        visited.add(current_node)

        # Goal check
        if current_node == goal:
            path = []
            node = current_node
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            print(f"\nGoal reached!  Path: {' -> '.join(path)}  |  Total cost: {g_costs[goal]}")
            return path

        # Standard A* neighbor expansion
        for neighbor, cost in graph[current_node].items():
            new_g = g_costs[current_node] + cost
            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor]   = new_g
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_g + heuristic[neighbor]))

        # ── Dynamic cost update at a random step interval ──────────────────────
        if step >= next_update_at and update_count < max_updates:
            update_count += 1
            delay = random.uniform(0.3, 1.2)          # random real-time interval
            print(f"\n{'=' * 52}")
            print(f"  Dynamic Update #{update_count}  (triggered at step {step}, delay={delay:.2f}s)")
            time.sleep(delay)

            changed = update_edge_costs(graph)
            if changed:
                display = {f"{u}->{v}": f"{old}->{new}" for (u, v), (old, new) in changed.items()}
                print(f"  Edge changes: {display}")

                for (u, v), (old_cost, new_cost) in changed.items():
                    if u not in g_costs:
                        # u not yet reached; the updated cost will be used naturally
                        continue

                    new_g_v = g_costs[u] + new_cost

                    if new_cost < old_cost:
                        # Cost decreased: check whether this opens a better path to v
                        if new_g_v < g_costs.get(v, float('inf')):
                            print(f"  Improvement {u}->{v}: re-opening '{v}'  "
                                  f"(g: {g_costs.get(v)} -> {new_g_v})")
                            g_costs[v]   = new_g_v
                            came_from[v] = u
                            visited.discard(v)
                            frontier.append((v, new_g_v + heuristic[v]))
                            # Cascade the improvement to v's downstream tree
                            propagate_cost_change(v, g_costs, came_from, visited,
                                                  frontier, graph, heuristic)

                    else:
                        # Cost increased: if v's best-known path runs through u, it is now
                        # invalid — re-open v and propagate the higher cost downstream
                        if came_from.get(v) == u:
                            print(f"  Degradation {u}->{v}: re-evaluating '{v}'  "
                                  f"(g: {g_costs.get(v)} -> {new_g_v})")
                            g_costs[v] = new_g_v
                            visited.discard(v)
                            frontier.append((v, new_g_v + heuristic[v]))
                            propagate_cost_change(v, g_costs, came_from, visited,
                                                  frontier, graph, heuristic)
            else:
                print("  No edges changed this interval.")

            next_update_at = step + random.randint(2, 4)
            print(f"  Resuming search  (next update around step {next_update_at})")
            print('=' * 52 + '\n')
        # ───────────────────────────────────────────────────────────────────────

    print("\nGoal not found")
    return None


# Run Dynamic A* Search
dynamic_a_star(graph, 'A', 'G', max_updates=3)