with open("input.txt", "r") as f:
    f = f.read().split("\n\n")
    g = []
    for i in f:
        g.append(
            [
                tuple([(int(k[3:])) for k in j.split(":")[1].split(",")])
                for j in i.split("\n")
            ]
        )

    tokens = 0
    for i in g:
        print(i)
        times = 0
        B = (i[0][0] * (10**13 + i[2][1]) - i[0][1] * (10**13 + i[2][0])) / (i[0][0] * i[1][1] - i[0][1] * i[1][0])
        A = ((10**13 + i[2][1]) - B * i[1][1])/i[0][1]
        
        if A.is_integer() and B.is_integer():
            tokens += A*3 + B
        print(A, B)

    print(tokens)
