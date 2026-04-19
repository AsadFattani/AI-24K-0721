
import math

class Node:
	def __init__(self, name=None, value=None):
		self.name = name
		self.value = value
		self.children = []
		self.minimax_value = None

def build_tree():
	root = Node('Root')
	attack = Node('Attack')
	defend = Node('Defend')
	gather = Node('Gather')
	root.children = [attack, defend, gather]

	a1 = Node('A1')
	a2 = Node('A2')
	d1 = Node('D1')
	d2 = Node('D2')
	g1 = Node('G1')
	g2 = Node('G2')
	attack.children = [a1, a2]
	defend.children = [d1, d2]
	gather.children = [g1, g2]

	a1.children = [Node(None, 5), Node(None, 6)]
	a2.children = [Node(None, 7), Node(None, 4)]
	d1.children = [Node(None, 3), Node(None, 8)]
	d2.children = [Node(None, 6), Node(None, 2)]
	g1.children = [Node(None, 1), Node(None, 9)]
	g2.children = [Node(None, 4), Node(None, 7)]

	return root

# Minimax algorithm
def minimax(node, depth, maximizing_player):
	if depth == 0 or not node.children:
		return node.value
	if maximizing_player:
		value = -math.inf
		for child in node.children:
			value = max(value, minimax(child, depth-1, False))
		node.minimax_value = value
		return value
	else:
		value = math.inf
		for child in node.children:
			value = min(value, minimax(child, depth-1, True))
		node.minimax_value = value
		return value

# Alpha-Beta Pruning algorithm
def alpha_beta(node, depth, alpha, beta, maximizing_player, ab_trace=None, pruned=None):
	if ab_trace is not None:
		ab_trace.append((node.name, alpha, beta))
	if depth == 0 or not node.children:
		return node.value
	if maximizing_player:
		value = -math.inf
		for child in node.children:
			value = max(value, alpha_beta(child, depth-1, alpha, beta, False, ab_trace, pruned))
			alpha = max(alpha, value)
			if beta <= alpha:
				if pruned is not None:
					pruned.append(child.name)
				break
		node.minimax_value = value
		return value
	else:
		value = math.inf
		for child in node.children:
			value = min(value, alpha_beta(child, depth-1, alpha, beta, True, ab_trace, pruned))
			beta = min(beta, value)
			if beta <= alpha:
				if pruned is not None:
					pruned.append(child.name)
				break
		node.minimax_value = value
		return value

def count_nodes(node):
	if not node.children:
		return 1
	return 1 + sum(count_nodes(child) for child in node.children)

root = build_tree()
depth = 3

# a) Minimax
minimax_value = minimax(root, depth, True)
print(f"a) Minimax value at root: {minimax_value}")
print(f"   Best action for MAX: ", end='')
for child in root.children:
    if child.minimax_value == minimax_value:
        print(child.name)

# b) Alpha-Beta Pruning
ab_trace = []
pruned = []
root_ab = build_tree()  # fresh tree for AB
ab_value = alpha_beta(root_ab, depth, -math.inf, math.inf, True, ab_trace, pruned)
print(f"\nb) Alpha-Beta value at root: {ab_value}")
print("   Alpha-Beta trace (node, alpha, beta):")
for entry in ab_trace:
    print(f"   {entry}")

# c) Pruned branches
print(f"\nc) Pruned branches: {pruned}")

# d) Node counts
print(f"\nd) Nodes evaluated in Minimax: {count_nodes(root)}")
print(f"   Nodes evaluated in Alpha-Beta: {len(ab_trace)}")

# e) Explanation
print("\ne) Alpha-Beta Pruning improves efficiency by pruning branches that cannot affect the final decision, reducing the number of nodes evaluated compared to standard Minimax.")
