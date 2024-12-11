def flatten_array(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            result.append(item)
    return result

with open("input.txt", "r") as f:
    f = f.readline().split(" ")
    
    for j in range(25):
        for i in range(len(f)):
            if int(f[i]) == 0:
                f[i] = "1"
            elif len(f[i])%2 == 0:
                f[i] = [str(int(f[i][:len(f[i])//2])), str(int(f[i][len(f[i])//2:]))]
            else:
                f[i] = str(int(f[i]) * 2024)
                
        f = flatten_array(f)
    
    print(len(f))