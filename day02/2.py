def safe(line):
    safe = True
    if line[1] - line[0] > 0:
        for i in range(len(line) - 1):
            if not 1 <= line[i +1] - line[i] <=3:
                safe = False
    elif line[1] - line[0] < 0:
        for i in range(len(line) - 1):
            if not -3 <= line[i +1] - line[i] <= -1:
                safe = False
    else:
        safe = False

    return safe


with open("input.txt", "r") as f:
    f = f.readlines()

    s_cnt = 0

    for l in f:
        l = l.split()
        l =  [int(a) for a in l]
        if safe(l):
            s_cnt += 1
        else:
            for i in l:
                a = list(l).copy()
                a.remove(i)
                print(l, a, safe(a))
                if safe(a):
                    s_cnt += 1
                    break



    print(s_cnt)