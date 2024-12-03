import re

def mul(a, b):
    return a*b

e = True
def do():
    global e 
    e = True

def don_t():
    global e
    e = False

with open("input.txt", "r") as f:
    f = f.readlines()[0]

    f = f.replace("don't", "don_t")

    m = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don_t\(\)", f)

    s = 0
    for l in m:
        print(e, l)
        if "mul" in l:
            s += eval(l) if e else 0
        else:
            eval(l)


    print(s)