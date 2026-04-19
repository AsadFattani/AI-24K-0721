
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import numpy as np

np.random.seed(42)
num_cities = 10
coords = np.random.rand(num_cities, 2) * 100 

def compute_euclidean_distance_matrix(locations):
	size = len(locations)
	matrix = {}
	for from_node in range(size):
		matrix[from_node] = {}
		for to_node in range(size):
			if from_node == to_node:
				matrix[from_node][to_node] = 0
			else:
				matrix[from_node][to_node] = int(
					np.linalg.norm(locations[from_node] - locations[to_node])
				)
	return matrix

distance_matrix = compute_euclidean_distance_matrix(coords)

manager = pywrapcp.RoutingIndexManager(num_cities, 1, 0)
routing = pywrapcp.RoutingModel(manager)

def distance_callback(from_index, to_index):
	from_node = manager.IndexToNode(from_index)
	to_node = manager.IndexToNode(to_index)
	return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
	routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

solution = routing.SolveWithParameters(search_parameters)

def print_solution(manager, routing, solution):
	print("Optimal path for 10 cities:")
	index = routing.Start(0)
	route = []
	route_distance = 0
	while not routing.IsEnd(index):
		node = manager.IndexToNode(index)
		route.append(node)
		previous_index = index
		index = solution.Value(routing.NextVar(index))
		route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
	route.append(manager.IndexToNode(index))  # return to start
	print(" -> ".join(str(city) for city in route))
	print(f"Total distance: {route_distance}")

if solution:
	print_solution(manager, routing, solution)
else:
	print("No solution found.")
