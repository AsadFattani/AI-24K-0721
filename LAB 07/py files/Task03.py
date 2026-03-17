# Genetic Algorithm for TSP (10 cities)
import random
import math

# Number of cities
NUM_CITIES = 10

# Generate random coordinates for cities
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(NUM_CITIES)]

def distance(city1, city2):
	return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def total_distance(tour):
	return sum(distance(cities[tour[i]], cities[tour[(i+1)%NUM_CITIES]]) for i in range(NUM_CITIES))

# Genetic Algorithm parameters
POP_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.1
ELITE_SIZE = 5

def create_tour():
	tour = list(range(NUM_CITIES))
	random.shuffle(tour)
	return tour

def crossover(parent1, parent2):
	start, end = sorted(random.sample(range(NUM_CITIES), 2))
	child = [None]*NUM_CITIES
	child[start:end] = parent1[start:end]
	ptr = 0
	for city in parent2:
		if city not in child:
			while child[ptr] is not None:
				ptr += 1
			child[ptr] = city
	return child

def mutate(tour):
	if random.random() < MUTATION_RATE:
		i, j = random.sample(range(NUM_CITIES), 2)
		tour[i], tour[j] = tour[j], tour[i]
	return tour

def select(population, fitnesses):
	# Tournament selection
	selected = []
	for _ in range(len(population)):
		i, j = random.sample(range(len(population)), 2)
		winner = population[i] if fitnesses[i] < fitnesses[j] else population[j]
		selected.append(winner)
	return selected

def genetic_algorithm():
	population = [create_tour() for _ in range(POP_SIZE)]
	for gen in range(GENERATIONS):
		fitnesses = [total_distance(tour) for tour in population]
		# Elitism
		elite_indices = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i])[:ELITE_SIZE]
		new_population = [population[i][:] for i in elite_indices]
		# Selection
		selected = select(population, fitnesses)
		# Crossover and mutation
		while len(new_population) < POP_SIZE:
			p1, p2 = random.sample(selected, 2)
			child = crossover(p1, p2)
			child = mutate(child)
			new_population.append(child)
		population = new_population
		if (gen+1) % 100 == 0:
			print(f"Generation {gen+1}: Best distance = {min(fitnesses):.2f}")
	# Final result
	fitnesses = [total_distance(tour) for tour in population]
	best_idx = min(range(len(fitnesses)), key=lambda i: fitnesses[i])
	print("Best tour:", population[best_idx])
	print("Best distance:", fitnesses[best_idx])
	print("City coordinates:", cities)


genetic_algorithm()
