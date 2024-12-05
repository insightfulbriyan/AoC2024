with open("rules.txt", "r") as r, open("orders.txt", "r") as o:
    r = [i.split("|") for i in r.read().split("\n")]
    o = [i.split(",") for i in o.read().split("\n")]
    
    
    s = 0
    
    for update in o:
        status = True
        for check in r:
            if check[0] not in update:
                continue
            
            if check[1] not in update:
                continue
            
            if update.index(check[0]) > update.index(check[1]):
                status = False
                break
            
        if status:
            s += int(update[int(len(update)/2)])
                
    print(s)