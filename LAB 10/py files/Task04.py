import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]
state_to_idx = {state: i for i, state in enumerate(states)}

transition_matrix = np.array([
	[0.7, 0.2, 0.1],  # Sunny -> Sunny, Cloudy, Rainy
	[0.3, 0.4, 0.3],  # Cloudy -> Sunny, Cloudy, Rainy
	[0.2, 0.3, 0.5],  # Rainy -> Sunny, Cloudy, Rainy
])

def simulate_weather(start_state, days, transition_matrix):
	current_state = state_to_idx[start_state]
	weather_sequence = [current_state]
	for _ in range(days - 1):
		current_state = np.random.choice(
			[0, 1, 2], p=transition_matrix[current_state]
		)
		weather_sequence.append(current_state)
	return weather_sequence

np.random.seed(42)
simulated_sequence = simulate_weather("Sunny", 10, transition_matrix)
simulated_weather = [states[i] for i in simulated_sequence]
print("Simulated weather for 10 days:", simulated_weather)

def estimate_rainy_probability(trials=10000):
	count = 0
	for _ in range(trials):
		seq = simulate_weather("Sunny", 10, transition_matrix)
		rainy_days = sum(1 for s in seq if s == state_to_idx["Rainy"])
		if rainy_days >= 3:
			count += 1
	return count / trials

prob = estimate_rainy_probability()
print(f"Probability of at least 3 rainy days in 10 days: {prob:.4f}")
