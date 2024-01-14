def check(park_grid):
    for i in range(3):
        if park_grid[i][0] == park_grid[i][1] == park_grid[i][2] and park_grid[i][0] != '.':
            return park_grid[i][0]
        if park_grid[0][i] == park_grid[1][i] == park_grid[2][i] and park_grid[0][i] != '.':
            return park_grid[0][i]

    if park_grid[0][0] == park_grid[1][1] == park_grid[2][2] and park_grid[0][0] != '.':
        return park_grid[0][0]
    if park_grid[0][2] == park_grid[1][1] == park_grid[2][0] and park_grid[0][2] != '.':
        return park_grid[0][2]

    return 'DRAW'

t = int(input())

for j in range(t):
    park_grid = [input() for j in range(3)]
    result = check(park_grid)
    print(result)
