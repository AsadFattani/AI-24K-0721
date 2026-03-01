#------------------1------------------>

class MazeAgent:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = None
        self.goal = None
        self.find_start_goal()

    def find_start_goal(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'S':
                    self.start = (i, j)
                elif self.maze[i][j] == 'G':
                    self.goal = (i, j)

    def valid_move(self, x, y):
        return (0 <= x < self.rows and
                0 <= y < self.cols and
                self.maze[x][y] != 1)

    # -------------------------------
    # Depth Limited Depth First Search
    # -------------------------------
    def depth_limited_dfs(self, limit):
        stack = [(self.start, 0, [self.start])]
        visited = set()

        while stack:
            (x, y), depth, path = stack.pop()

            if (x, y) == self.goal:
                return path

            if depth < limit:
                visited.add((x, y))

                moves = [(-1,0), (1,0), (0,-1), (0,1)]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if self.valid_move(nx, ny) and (nx, ny) not in visited:
                        stack.append(((nx, ny), depth + 1, path + [(nx, ny)]))

        return None

    # -------------------------------
    # Iterative Deepening Search
    # -------------------------------
    def iterative_deepening_search(self, max_depth):
        for depth in range(max_depth + 1):
            result = self.depth_limited_dfs(depth)
            if result is not None:
                return result
        return None


maze = [
    ['S', 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 'G'],
    [1, 1, 0, 1, 1]
]

agent = MazeAgent(maze)

print("Depth Limited DFS Output:")
print(agent.depth_limited_dfs(6))

print("\nIterative Deepening Search Output:")
print(agent.iterative_deepening_search(10))


# Why Iterative Deepening Search Is Better

# 1. Limited Memory
# - Uses DFS internally
# - Stores very few nodes
# 2. Unknown Goal Depth
# - Does not assume where goal is
# - Increases depth step by step
# 3. Dead-End Handling
# - Avoids getting stuck in deep tunnels
# - Restarts search safely
# 4. Completeness
# - Guaranteed to find goal if it exists
# - Finds shortest path for equal cost moves

