with open("input.txt", "r") as f:
    f = f.readlines()

    l, r = [], []

    for line in f:
        l.append(int(line.split("   ")[0]))
        r.append(int(line.split("   ")[1]))

    l.sort()
    r.sort()

    distance = 0
    for a, b in zip(l, r):
        distance += abs(a - b)

    print(distance)