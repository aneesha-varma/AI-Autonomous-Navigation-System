import numpy as np

def create_grid(size):
    grid = np.zeros((size, size))
    return grid

def add_obstacles(grid, obstacle_ratio=0.2):
    size = grid.shape[0]
    num_obstacles = int(size * size * obstacle_ratio)

    for _ in range(num_obstacles):
        x, y = np.random.randint(0, size, 2)
        grid[x][y] = 1

    return grid