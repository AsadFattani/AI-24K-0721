import heapq

class UtilityBasedAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.path = []
        self.total_cost = 0

    def percieve(self):
        return self.start
    
    def utility(self, cost):
        return -cost
    
    def act(self):
        queue = [(0, self.start, [self.start])]
        visited = set()
        while queue:
            cost, node, path = heapq.heappop(queue)
            if node == self.goal:
                self.path = path
                self.total_cost = cost
                print(f"Goal reavhed! Path: {path}, Total cost: {cost}")
                return True
            if node in visited:
                continue 
            visited.add(node)
            for neighbor, edge_cost in self.graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, neighbor, path + [neighbor]))
        print("Goal not reachable.")
        return False
    
    def run(self):
        self.act()

graph = {
    'A': {'B': 5, 'C': 4},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 4, 'G': 2},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {'J': 1},
    'I': {}
}

agent = UtilityBasedAgent(graph, 'A', 'J')
agent.run()