with open("input.txt", "r") as f:
    f = f.read().split("\n\n")
    g = []
    for i in f:
        g.append([tuple([(int(k[3:])) for k in j.split(":")[1].split(",")]) for j in i.split("\n")])
        
    tokens = 0
    for i in g:
        print(i)
        times = 0
        while times <= 200:
            # človeška neumnost ne pozna meja
            for a in range(min(100, times + 1)):
                if i[0][0] * a + i[1][0] *(times - a) == i[2][0] and i[0][1] * a + i[1][1] *(times - a) == i[2][1]:
                    tokens += 3*a + times - a
            times += 1
            
    print(tokens)