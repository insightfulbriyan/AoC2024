def find_sublist(lst, sublist):
    n = len(sublist)
    for i in range(len(lst) - n + 1):
        if lst[i:i + n] == sublist:
            return i
    return 0

with open("input.txt", "r") as f:
    f = f.readline()
    
    disk = []
    for i in range(int(len(f)/2)):
        disk += [i]*int(f[2*i])
        disk += "."*int(f[2*i+1])
        
    #print(disk)
    p = len(disk) - 1
    #print("".join(map(str, disk)))
    #print(" "*p + "^")
    while p > 1:
        if disk[p] == ".":
            p -= 1
        else:
            file_len = p - disk.index(disk[p]) + 1
            s = find_sublist(disk[:p], ["."]*file_len)
            #print(f"{disk[p]=}, {disk.index(disk[p])=}, {p=}, {file_len=}, {s=}")
            if s:
                temp = disk[p-file_len+1:p+1]
                disk[p-file_len+1:p+1] = ["."] * file_len
                disk[s:s+file_len] = temp
            p -= file_len
        
        #print("".join(map(str, disk)))
        #print(" "*p + "^")
        

    #print(disk)
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        checksum += i*int(disk[i])
        
    print(checksum)