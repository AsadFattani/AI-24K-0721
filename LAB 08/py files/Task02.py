import math
class Node:
	def __init__(self, name, value=None):
		self.name = name
		self.value = value
		self.children = []
		self.minimax_value = None

# Minimax algorithm implementation
class Minimax:
	def __init__(self):
		self.visited = []

	def minimax(self, node, maximizing_player=True):
		if not node.children:
			self.visited.append(node.name)
			node.minimax_value = node.value
			return node.value
		if maximizing_player:
			value = -math.inf
			for child in node.children:
				value = max(value, self.minimax(child, False))
			node.minimax_value = value
			self.visited.append(node.name)
			return value
		else:
			value = math.inf
			for child in node.children:
				value = min(value, self.minimax(child, True))
			node.minimax_value = value
			self.visited.append(node.name)
			return value

# Alpha-Beta Pruning implementation
class AlphaBeta:
	def __init__(self):
		self.visited = []
		self.pruned = []

	def alphabeta(self, node, alpha=-math.inf, beta=math.inf, maximizing_player=True):
		if not node.children:
			self.visited.append(node.name)
			node.minimax_value = node.value
			return node.value
		if maximizing_player:
			value = -math.inf
			for child in node.children:
				v = self.alphabeta(child, alpha, beta, False)
				value = max(value, v)
				alpha = max(alpha, value)
				if beta <= alpha:
					# Prune remaining children
					idx = node.children.index(child)
					for pruned_child in node.children[idx+1:]:
						self.pruned.append(pruned_child.name)
					break
			node.minimax_value = value
			self.visited.append(node.name)
			return value
		else:
			value = math.inf
			for child in node.children:
				v = self.alphabeta(child, alpha, beta, True)
				value = min(value, v)
				beta = min(beta, value)
				if beta <= alpha:
					idx = node.children.index(child)
					for pruned_child in node.children[idx+1:]:
						self.pruned.append(pruned_child.name)
					break
			node.minimax_value = value
			self.visited.append(node.name)
			return value

root = Node('Start')
stop = Node('Stop')
go = Node('Go')
turn = Node('Turn')
root.children = [stop, go, turn]

stop.children = [Node('Stop-1', 6), Node('Stop-2', 7)]
go.children = [Node('Go-1', 2), Node('Go-2', 4)]
turn.children = [Node('Turn-1', 8), Node('Turn-2', 3)]

# --- Minimax ---
minimax_solver = Minimax()
best_value = minimax_solver.minimax(root, maximizing_player=True)

print("Minimax Traversal Order:", minimax_solver.visited)
print("Minimax Value at Root (Best Action Value):", best_value)
print("Action Values:")
for action in root.children:
	print(f"{action.name}: {action.minimax_value}")

# --- Alpha-Beta Pruning ---
alphabeta_solver = AlphaBeta()
ab_value = alphabeta_solver.alphabeta(root, maximizing_player=True)

print("\nAlpha-Beta Traversal Order:", alphabeta_solver.visited)
print("Alpha-Beta Value at Root (Best Action Value):", ab_value)
print("Action Values:")
for action in root.children:
	print(f"{action.name}: {action.minimax_value}")

print("Pruned Branches:", alphabeta_solver.pruned)
print("Number of Nodes Not Evaluated due to Pruning:", len(alphabeta_solver.pruned))
