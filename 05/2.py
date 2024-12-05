with open("rules.txt", "r") as r, open("orders.txt", "r") as o:
    r = [i.split("|") for i in r.read().split("\n")]
    o = [i.split(",") for i in o.read().split("\n")]
    
    
    s = 0
    
    incorrect = []
    for update in o:
        for check in r:
            if check[0] not in update:
                continue
            
            if check[1] not in update:
                continue
            
            if update.index(check[0]) > update.index(check[1]):
                incorrect.append(update)
                break
          
    for _ in range(5):
        for update in incorrect:
            for check in r:
                if check[0] not in update:
                    continue
                
                if check[1] not in update:
                    continue
                
                if update.index(check[0]) > update.index(check[1]):
                    temp = update[update.index(check[0])]
                    update[update.index(check[0])] = update[update.index(check[1])]
                    update[update.index(check[1])] = temp
                
    for update in o:
        for check in r:
            if check[0] not in update:
                continue
            
            if check[1] not in update:
                continue
            
            if update.index(check[0]) > update.index(check[1]):
                print(update, "\n\n", check)
            
    for u in incorrect:
        print(u)
        print(int(u[int(len(u)/2)]))
        print()
        s += int(u[int(len(u)/2)])
    print(s)