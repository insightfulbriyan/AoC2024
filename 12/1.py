def findAregion(grid, visited, x, y, letter):
    stack = [(x, y)]
    region = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == letter:
                visited[nx][ny] = True
                stack.append((nx, ny))
                region.append((nx, ny))
    return region


def calculatePerimeter(grid, region_cells):
    perimeter = 0
    for x, y in region_cells:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != grid[x][y]:
                perimeter += 1
    return perimeter

with open("input.txt", "r") as f:
    f = [[j for j in i] for i in f.read().split("\n")]
    
    m, n = len(f), len(f[0])
    visited = [[False] * n for _ in range(m)]
    
    regions = []
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                # Start a new region
                visited[i][j] = True
                regions.append(findAregion(f, visited, i, j, f[i][j]))
                
    cost = 0
    for i in regions:
        cost += calculatePerimeter(f, i)*len(i)
        print(f[i[0][0]][i[0][1]], len(i), cost)