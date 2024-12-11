with open("input.txt", "r") as f:
    f = f.readline()
    
    disk = []
    for i in range(int(len(f)/2)):
        disk += [i]*int(f[2*i])
        disk += "."*int(f[2*i+1])
        
    # print(disk)
    while "." in disk:
        c = disk.pop()
        if c == ".":
            continue
        disk[disk.index(".")] = c

    # print(disk)
    checksum = 0
    for i in range(len(disk)):
        checksum += i*int(disk[i])
        
    print(checksum)