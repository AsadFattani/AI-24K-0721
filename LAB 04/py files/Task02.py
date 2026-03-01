

graph = {
    '1': {'2': 10, '3': 15, '4': 20},
    '2': {'1': 10, '4': 25, '3': 35},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}

def tsp(graph, start):
    cities = [k for k in graph.keys() if k != start]
    min_path = None
    min_cost = float('inf')
    
    def permute(arr, l ,r):
        nonlocal min_cost, min_path
        if l == r:
            perm = arr[:]
            current_cost = 0
            k = start 
            for j in perm:
                current_cost += graph[k][j]
                k = j
            current_cost += graph[k][start]
            path_tuple = [start] + perm + [start]
            if current_cost < min_cost:
                min_cost = current_cost
                min_path = path_tuple
        else:
            for i in range(l, r+1):
                arr[l], arr[i] = arr[i], arr[l]
                permute(arr, l+1, r)
                arr[l], arr[i] = arr[i], arr[l]
    
    permute(cities, 0, len(cities)-1)
    return min_path, min_cost

path, cost = tsp(graph, '1')

print("Shortest path:", " -> ".join(path))
print("Minimum cost:", cost)