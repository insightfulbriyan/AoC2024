dirs = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v":(1, 0)}

with open("input.txt", "r") as f:
    grid, moves = f.read().split("\n\n")
    grid = [[j for j in i] for i in grid.split("\n")]
    moves = [i for i in moves.replace("\n", "")]
    
    x, y = 24, 24
    for m in moves:
        dx, dy = dirs[m]
        n = 1
        while grid[x + n*dx][y + n*dy] == "O":
            n += 1
            
        if grid[x + n*dx][y + n*dy] == "#":
            continue
        
        grid[x + n*dx][y + n*dy] = "O"
        grid[x][y] = "."
        grid[x + dx][y + dy] = "@"
        x += dx
        y += dy
        
    gps = 0   
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "O":
                gps += 100*x + y
    
    print(gps)