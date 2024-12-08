with open("input.txt", "r") as f:
    f = [list(i.strip()) for i in f.readlines()]
    
    guard = [87, 46] 
        
    while f[guard[0]][guard[1]] != "0":
        if f[guard[0]][guard[1]] == "1":
            print("1")
            if f[guard[0]-1][guard[1]] == "#":
                f[guard[0]][guard[1]] = "2"
                continue
            elif f[guard[0]-1][guard[1]] == "0":
                break
            f[guard[0]][guard[1]] = "S"
            guard[0] += -1
            f[guard[0]][guard[1]] = "1"
            
        elif f[guard[0]][guard[1]] == "2":
            print("2")
            if f[guard[0]][guard[1]+1] == "#":
                f[guard[0]][guard[1]] = "3"
                continue
            elif f[guard[0]][guard[1]+1] == "0":
                break
            f[guard[0]][guard[1]] = "S"
            guard[1] += +1
            f[guard[0]][guard[1]] = "2"
            
        elif f[guard[0]][guard[1]] == "3":
            print("3")
            if f[guard[0]+1][guard[1]] == "#":
                f[guard[0]][guard[1]] = "4"
                continue
            elif f[guard[0]+1][guard[1]] == "0":
                break
            f[guard[0]][guard[1]] = "S"
            guard[0] += +1
            f[guard[0]][guard[1]] = "3"
            
        elif f[guard[0]][guard[1]] == "4":
            print("4")
            if f[guard[0]][guard[1]-1] == "#":
                f[guard[0]][guard[1]] = "1"
                continue
            elif f[guard[0]][guard[1]-1] == "0":
                break
            f[guard[0]][guard[1]] = "S"
            guard[1] += -1
            f[guard[0]][guard[1]] = "4"
            
        else:
            print("I'm stuck")
            
            
    for l in f:
        print("".join(l))