import matplotlib.pyplot as plt

def plot(grid, path, start, goal):
    plt.imshow(grid, cmap='gray')

    if path:
        x, y = zip(*path)
        plt.plot(y, x, color='blue')

    plt.scatter(start[1], start[0], color='green')
    plt.scatter(goal[1], goal[0], color='red')

    plt.show()