 
from ortools.sat.python import cp_model
import math

grid = [[0]*5 for _ in range(5)]

start = (1, 1)
goal = (4, 4)

moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

model = cp_model.CpModel()

MAX_STEPS = 7 

x = [model.NewIntVar(0, 4, f'x{t}') for t in range(MAX_STEPS)]
y = [model.NewIntVar(0, 4, f'y{t}') for t in range(MAX_STEPS)]

step_used = [model.NewBoolVar(f'step_used_{t}') for t in range(MAX_STEPS)]

model.Add(x[0] == start[0])
model.Add(y[0] == start[1])
model.Add(step_used[0] == 1)

goal_reached = [model.NewBoolVar(f'goal_at_{t}') for t in range(MAX_STEPS)]
for t in range(MAX_STEPS):
    model.Add(x[t] == goal[0]).OnlyEnforceIf(goal_reached[t])
    model.Add(y[t] == goal[1]).OnlyEnforceIf(goal_reached[t])
    model.Add(step_used[t] == 1).OnlyEnforceIf(goal_reached[t])
model.AddBoolOr(goal_reached)

for t in range(MAX_STEPS-1):
    model.AddImplication(goal_reached[t], goal_reached[t+1])
    model.Add(x[t+1] == goal[0]).OnlyEnforceIf(goal_reached[t])
    model.Add(y[t+1] == goal[1]).OnlyEnforceIf(goal_reached[t])

for t in range(MAX_STEPS-1):
    move_bools = []
    for dx, dy in moves:
        valid = model.NewBoolVar(f'move_{t}_{dx}_{dy}')
        move_bools.append(valid)
        model.Add(x[t+1] == x[t] + dx).OnlyEnforceIf(valid)
        model.Add(y[t+1] == y[t] + dy).OnlyEnforceIf(valid)
        model.Add(step_used[t+1] == 1).OnlyEnforceIf(valid)
        model.Add(step_used[t] == 1).OnlyEnforceIf(valid)
        model.Add(goal_reached[t] == 0).OnlyEnforceIf(valid)
    model.AddExactlyOne(move_bools + [goal_reached[t]]).OnlyEnforceIf(step_used[t])
    model.Add(x[t+1] == x[t]).OnlyEnforceIf(step_used[t+1].Not())
    model.Add(y[t+1] == y[t]).OnlyEnforceIf(step_used[t+1].Not())

for t in range(MAX_STEPS):
    model.Add(x[t] >= 0)
    model.Add(x[t] <= 4)
    model.Add(y[t] >= 0)
    model.Add(y[t] <= 4)
    # No obstacles in this example, but if grid[i][j]==1, forbid (i,j)
    # for i in range(5):
    #     for j in range(5):
    #         if grid[i][j] == 1:
    #             model.Add((x[t] != i) | (y[t] != j))

model.Minimize(sum(step_used))

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
    path = []
    for t in range(MAX_STEPS):
        if solver.Value(step_used[t]):
            px = solver.Value(x[t])
            py = solver.Value(y[t])
            path.append((px, py))
            if (px, py) == goal:
                break
    print("Shortest diagonal path:", path)
    print("Number of steps:", len(path)-1)
    print("Total cost:", round((len(path)-1) * math.sqrt(2), 3))
else:
    print("No path found.")