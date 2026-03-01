
tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : [],
    'F' : ['I'],
    'G' : [],
    'H' : [],
    'I' : []
}

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20, 'E': 5},
    'B': {'A': 10, 'D': 25, 'C': 35, 'F': 12},
    'C': {'A': 15, 'B': 35, 'D': 30, 'G': 8},
    'D': {'A': 20, 'B': 25, 'C': 30, 'H': 14},
    'E': {'A': 5, 'I': 7},
    'F': {'B': 12, 'J': 9},
    'G': {'C': 8, 'K': 11},
    'H': {'D': 14, 'L': 6},
    'I': {'E': 7},
    'J': {'F': 9},
    'K': {'G': 11},
    'L': {'H': 6}
}

def dls(graph, node, goal, depth_limit, visited):
    if depth_limit < 0:
        return None
    
    visited.append(node)

    if node == goal:
        return visited.copy()
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            path = dls(graph, neighbor, goal, depth_limit - 1, visited)
            if path:
                return path
            
    visited.pop()
    return None

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = []
        path = dls(graph, start, goal, depth, visited)

        if path:
            print("Goal Found at depth", depth)
            print("Path:", " -> ".join(path))
            return path
    
    print("Goal Not fount with depth limit of", max_depth)
    return None

start_node = 'A'
goal_node = 'D'
max_depth = 5

print("Iterative Deepening Search(tree):")
ids(tree, start_node, goal_node, max_depth)

goal_node = 'K'
print("\nIterative Deepening Search(graph):")
ids(graph, start_node, goal_node, max_depth)



