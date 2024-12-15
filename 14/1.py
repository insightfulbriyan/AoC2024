example = False
with open("ex_input.txt" if example else "input.txt", "r") as f:
    f = [
        [tuple([int(k) for k in j[2:].split(",")]) for j in i.split(" ")]
        for i in f.read().split("\n")
    ]

    h = 11 if example else 101
    v = 7 if example else 103

    grid = [[[]] * h for _ in range(v)]

    # initial
    for i in f:
        x = (i[0][0] + i[1][0] * 100) % h
        y = (i[0][1] + i[1][1] * 100) % v
        grid[y][x] = grid[y][x] + [i]

    one = [[[]] * (h//2) for _ in range(v//2)]
    two = [[[]] * (h//2) for _ in range(v//2)]
    three = [[[]] * (h//2) for _ in range(v//2)]
    four = [[[]] * (h//2) for _ in range(v//2)]

    for i in range(v//2):
        for j in range(h//2):
            one[i][j] = grid[i][j + h//2 + 1]
            two[i][j] = grid[i][j]
            three[i][j] = grid[i+v//2+1][j]
            four[i][j] = grid[i+v//2+1][j + h//2 + 1]
            
    on = 0
    tw = 0
    th = 0
    fo = 0
    for i in one:
        for c in i:
            on += len(c)
    for i in two:
        for c in i:
            tw += len(c)
    for i in three:
        for c in i:
            th += len(c)
    for i in four:
        for c in i:
            fo += len(c)
            
            
    print(on*tw*th*fo)