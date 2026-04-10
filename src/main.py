from grid import create_grid, add_obstacles
from astar import astar
from visualization import plot

SIZE = 20

grid = create_grid(SIZE)
grid = add_obstacles(grid)

start = (0, 0)
goal = (19, 19)

path = astar(grid, start, goal)

if path:
    print("Path found!")
else:
    print("No path found")

plot(grid, path, start, goal)