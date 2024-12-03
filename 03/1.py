import re

def mul(a, b):
    return a*b

with open("input.txt", "r") as f:
    f = f.readlines()[0]

    m = re.findall("mul[(][0-9]{1,3},[0-9]{1,3}[)]", f)

    s = 0
    for l in m:
        s += eval(l)

    print(s)