def flatten_array(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_array(item))  # Use recursion to flatten sublists
        else:
            result.append(item)
    return result

with open("input.txt", "r") as f:
    grid, moves = f.read().split("\n\n")
    grid = [
        flatten_array(
            [
                {"#": ["#", "#"], ".": [".", "."], "O": ["[", "]"], "@": ["@", "."]}[j]
                for j in i
            ]
        )
        for i in grid.split("\n")
    ]
    moves = [i for i in moves.replace("\n", "")]
    
    x, y = 24, 48
    grid[x][y] = "."
    
    for m in moves:
        # print(m)
        dx, dy = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[m]        
        x += dx
        y += dy
        
        if grid[x][y] == "#":
            x -= dx
            y -= dy
            continue
        
        if grid[x][y] in ["[", "]"]:
            Q = [(x - dx, y - dy)]
            SEEN = set()
            while Q:
                xx, yy = Q.pop(0)
                if (xx, yy) in SEEN:
                    continue
                SEEN.add((xx, yy))
                xxx, yyy = xx + dx, yy + dy
                if grid[xxx][yyy] == "#":
                    break
                elif grid[xxx][yyy] == "[":
                    Q.append((xxx, yyy))
                    assert grid[xxx][yyy + 1] == "]"
                    Q.append((xxx, yyy + 1))
                elif grid[xxx][yyy] == "]":
                    Q.append((xxx, yyy))
                    assert grid[xxx][yyy - 1] == "["
                    Q.append((xxx, yyy - 1))
            if grid[xxx][yyy] == "#":
                x -= dx
                y -= dy
                continue
            while len(SEEN) > 0:
                for xx, yy in sorted(SEEN):
                    xxx, yyy = xx + dx, yy + dy
                    if (xxx, yyy) not in SEEN:
                        assert grid[xxx][yyy] == "."
                        grid[xxx][yyy] = grid[xx][yy]
                        grid[xx][yy] = "."
                        SEEN.remove((xx, yy))
                        
                   
                   

    gps = 0   
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "[":
                gps += 100*x + y
    
    print(gps)
