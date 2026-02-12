import random
list = ["clean", "dirty"]

class Environment:
    def __init__(self):
        self.grid = [
            [random.choice(list) for _ in range(3)] for _ in range(3)
        ]
    
    def get_percept(self, row, col):
        return self.grid[row][col]
    
    def clean(self, row, col):
        self.grid[row][col] = 'clean'

    def display(self, ar, ac):
        print("Grid:")
        for i in range(3):
            row = []
            for j in range(3):
                if i == ar and j == ac:
                    row.append('_')  # agent
                else:
                    row.append(self.grid[i][j])
            print(" | ".join(row))
        print()
    
    def dynamicChange(self):
        self.grid = [
            [random.choice(list) for _ in range(3)] for _ in range(3)
        ]
        
class Agent:
    def act(self, percept):
        if percept == 'dirty':
            return 'clean'
        else:
            return 'move'
        

def run_agent(environment, agent, steps):
    row, col = 0, 0

    for i in range(steps):
        percept = environment.get_percept(row, col)
        action = agent.act(percept)

        print(f"Step {i+1}: Percept = {percept}, "
              f"Position = ({row},{col}), Action = {action}")
        print("It changed sucker")
        environment.dynamicChange()
        if action == 'clean':
            environment.clean(row, col)
        else:
            col += 1
            if col == 3:
                row += 1
                col = 0
            if row == 3:
                break

        environment.display(row, col)


environment = Environment()
agent = Agent()
run_agent(environment, agent, 9)