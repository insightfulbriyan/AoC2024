with open("input.txt", "r") as f:
    f = f.readlines()

    l, r = [], []

    for line in f:
        l.append(int(line.split("   ")[0]))
        r.append(int(line.split("   ")[1]))

    l.sort()
    r.sort()

    similarity = 0
    for a in l:
        similarity += a*r.count(a)

    print(similarity)