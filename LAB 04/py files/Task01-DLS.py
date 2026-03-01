class GoalBasedAgent:
    def __init__ (self, graph, start, goal, depth_limit):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.depth_limit = depth_limit
        self.visited = []
        self.path = []

    def percieve(self):
        return self.start
    
    def decide(self, current_node, depth):
        if depth > self.depth_limit or current_node == self.goal:
            return current_node
        return None
    
    def act(self, node, depth):
        self.visited.append(node)
        self.path.append(node)

        if depth > self.depth_limit:
            print (f"Depth limit reached at node {node}.")
            self.path.pop()
            self.visited.pop()
            return False
        
        if node == self.goal:
            print (f"Goal reached! Path: {self.path}")
            return True
        
        for neighbor in self.graph.get(node, []):
            if neighbor not in self.visited:
                if self.act(neighbor, depth + 1):
                    return True
        
        self.path.pop()
        self.visited.pop()
        return False
    
    def run(self):
        self.act(self.start, 0)
    
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : ['H'],
    'E' : [],
    'F' : ['I'],
    'G' : [],
    'H' : [],
    'I' : ['J']
}

agent = GoalBasedAgent(graph, 'A', 'J', 4)
agent.run()