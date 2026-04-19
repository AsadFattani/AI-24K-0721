
import math

class Node:
	def __init__(self, name, value=None):
		self.name = name
		self.value = value
		self.children = []
		self.minimax_value = None

class Environment:
	def __init__(self):
		self.root = Node('Root')
		zone_a = Node('Zone A')
		zone_b = Node('Zone B')
		self.root.children = [zone_a, zone_b]
		# Thief's options
		zone_a.children = [Node('A-Option1', 3), Node('A-Option2', 5)]
		zone_b.children = [Node('B-Option1', 2), Node('B-Option2', 9)]

	def get_percept(self, node):
		return node

	def print_states(self):
		print("All possible states and moves:")
		for zone in self.root.children:
			for thief in zone.children:
				print(f"Robot -> {zone.name}, Thief -> {thief.name.split('-')[1]}, Payoff: {thief.value}")

class MinimaxAgent:
	def __init__(self, depth):
		self.depth = depth
		self.computed_nodes = []

	def compute_minimax(self, node, depth, maximizing):
		if depth == 0 or not node.children:
			self.computed_nodes.append(node.name)
			return node.value
		if maximizing:
			value = -math.inf
			for child in node.children:
				value = max(value, self.compute_minimax(child, depth-1, False))
			node.minimax_value = value
			self.computed_nodes.append(node.name)
			return value
		else:
			value = math.inf
			for child in node.children:
				value = min(value, self.compute_minimax(child, depth-1, True))
			node.minimax_value = value
			self.computed_nodes.append(node.name)
			return value

	def act(self, percept, environment):
		print("\nMinimax computation:")
		best_value = -math.inf
		best_move = None
		for zone in percept.children:
			value = self.compute_minimax(zone, self.depth-1, False)
			print(f"If Robot chooses {zone.name}, Thief minimizes to: {value}")
			if value > best_value:
				best_value = value
				best_move = zone.name
		print(f"\nRobot should choose: {best_move} (guaranteed payoff: {best_value})")

def run_agent(agent, environment, start_node):
	percept = environment.get_percept(start_node)
	agent.act(percept, environment)

environment = Environment()
environment.print_states()
agent = MinimaxAgent(depth=2)
run_agent(agent, environment, environment.root)
