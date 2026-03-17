import random
import math

def total_distance(route, points):
    dist = 0
    for i in range(len(route) - 1):
        x1, y1 = points[route[i]]
        x2, y2 = points[route[i+1]]
        dist += math.hypot(x2 - x1, y2 - y1)
    return dist

def hill_climbing_route(points):
    n = len(points)
    route = list(range(n))
    random.shuffle(route)
    best_distance = total_distance(route, points)
    improved = True

    while improved:
        improved = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                new_route = route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                new_distance = total_distance(new_route, points)
                if new_distance < best_distance:
                    route = new_route
                    best_distance = new_distance
                    improved = True
        # If no improvement, exit
    return route, best_distance

    # Example input: list of coordinates
points = [
    (0, 0),
    (2, 3),
    (5, 4),
    (1, 1),
    (6, 2),
    (3, 5)
]
route, dist = hill_climbing_route(points)
print("Optimized route (by index):", route)
print("Route coordinates:", [points[i] for i in route])
print("Total distance:", dist)