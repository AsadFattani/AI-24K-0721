# Satellite Island Perimeter Calculation using OR-Tools

from ortools.sat.python import cp_model

grid = [
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
]

rows = len(grid)
cols = len(grid[0])

model = cp_model.CpModel()

x = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(model.NewBoolVar(f'x_{i}_{j}'))
    x.append(row)

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            model.Add(x[i][j] == 0)

def neighbors(i, j):
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < rows and 0 <= nj < cols:
            yield ni, nj

land_cells = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
if not land_cells:
    print("No land present.")
else:
    root = land_cells[0]
    flow = {}
    for i, j in land_cells:
        for ni, nj in neighbors(i, j):
            if grid[ni][nj] == 1:
                flow[(i, j, ni, nj)] = model.NewIntVar(0, rows*cols, f'flow_{i}_{j}_{ni}_{nj}')
    for i, j in land_cells:
        if (i, j) == root:
            continue
        inflow = []
        outflow = []
        for ni, nj in neighbors(i, j):
            if grid[ni][nj] == 1:
                if (ni, nj, i, j) in flow:
                    inflow.append(flow[(ni, nj, i, j)])
                if (i, j, ni, nj) in flow:
                    outflow.append(flow[(i, j, ni, nj)])
        model.Add(sum(inflow) - sum(outflow) == x[i][j])
    inflow = []
    outflow = []
    for ni, nj in neighbors(root[0], root[1]):
        if grid[ni][nj] == 1:
            if (ni, nj, root[0], root[1]) in flow:
                inflow.append(flow[(ni, nj, root[0], root[1])])
            if (root[0], root[1], ni, nj) in flow:
                outflow.append(flow[(root[0], root[1], ni, nj)])
    model.Add(sum(outflow) - sum(inflow) == sum(x[i][j] for i, j in land_cells) - 1)
    for (i, j, ni, nj), f in flow.items():
        model.Add(f <= x[i][j] * rows * cols)
        model.Add(f <= x[ni][nj] * rows * cols)

    model.Maximize(sum(x[i][j] for i, j in land_cells))

    # Solve
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        landmass = [[solver.Value(x[i][j]) for j in range(cols)] for i in range(rows)]
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if landmass[i][j]:
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i+di, j+dj
                        if not (0 <= ni < rows and 0 <= nj < cols) or not landmass[ni][nj]:
                            perimeter += 1
        print("Largest landmass:")
        for row in landmass:
            print(row)
        print(f"Perimeter: {perimeter}")
    else:
        print("No solution found.")
