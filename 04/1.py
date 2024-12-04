with open("input.txt", "r") as f:
    f = f.readlines()
    
    print(f[3])

    search_table = [
        [
            [1, 0],
            [2, 0],
            [3, 0],
        ],
        [
            [0, 1],
            [0, 2],
            [0, 3],
        ],
        [
            [-1, 0],
            [-2, 0],
            [-3, 0],
        ],
        [
            [0, -1],
            [0, -2],
            [0, -3],
        ],
        [
            [1, 1],
            [2, 2],
            [3, 3],
        ],
        [
            [-1, 1],
            [-2, 2],
            [-3, 3],
        ],
        [
            [-1, -1],
            [-2, -2],
            [-3, -3],
        ],
        [
            [1, -1],
            [2, -2],
            [3, -3],
        ],
    ]

    iks = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == "X":
                iks.append([i, j])
    count = 0
    for i,j in iks:
        for p in search_table:
            test = True
            for s, d in enumerate(p, start=1):
                if f[i+d[0]][j+d[1]] != "XMAS"[s]:
                    test = False
                    break
            count += test
        
    print(count)
                