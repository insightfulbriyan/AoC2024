with open("input.txt", "r") as f:
    f = [[int(j) for j in i] for i in f.read().split("\n")]

    trailhead_candidates = []
    for x in range(len(f)):
        for y in range(len(f[x])):
            if f[x][y] == 0:
                trailhead_candidates.append([x, y])

    score = 0
    for x, y in trailhead_candidates:
        ends = [[0] * len(f[0])] * len(f)

        trails = [[[x, y]], [], [], [], [], [], [], [], [], []]
        for i in range(1, 10):
            for a, b in trails[i - 1]:
                for da, db in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if (
                        0 <= a + da < len(f)
                        and 0 <= b + db < len(f[0])
                        and f[a + da][b + db] == i
                    ):
                        trails[i].append([a + da, b + db])
        score += len(set([tuple(i) for i in trails[9]]))
    print(score)
