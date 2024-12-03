with open("input.txt", "r") as f:
    f = f.readlines()

    s_cnt = 0

    for l in f:
        l = l.split()
        l =  [int(a) for a in l]
        safe = True
        if l[1] - l[0] > 0:
            for i in range(len(l) - 1):
                if not 1 <= l[i +1] - l[i] <=3:
                    safe = False
        elif l[1] - l[0] < 0:
            for i in range(len(l) - 1):
                if not -3 <= l[i +1] - l[i] <= -1:
                    safe = False
        else:
            safe = False
        s_cnt += safe

    print(s_cnt)