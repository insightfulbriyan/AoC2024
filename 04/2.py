with open("input.txt", "r") as f:
    f = f.readlines()

    search_table = [
        # M.M
        # .A.
        # S.S
        [
            [-1, -1],
            [-1, 1],
            [1, 1],
            [1, -1],
        ],
        # M.S
        # .A.
        # M.S
        [
            [-1, -1],
            [1, -1],
            [-1, 1],
            [1, 1],
        ],
        # S.M
        # .A.
        # S.M
        [
            [-1, 1],
            [1, 1],
            [1, -1],
            [-1, -1],
        ],
        # S.S
        # .A.
        # M.M
        [
            [1, -1],
            [1, 1],
            [-1, 1],
            [-1, -1],
        ],
    ]

    iks = []
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == "A":
                iks.append([i, j])

    print(iks)
    count = 0
    for i, j in iks:
        for p in search_table:
            test = True
            for s, d in enumerate(p):
                if f[i + d[0]][j + d[1]] != "MMSS"[s]:
                    test = False
                    break
            count += test
    print(count)
