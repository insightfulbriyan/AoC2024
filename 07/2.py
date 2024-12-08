def compute(values, signs):
    if not signs:
        return values[0]
    elif signs[0] == '0':
        values = [values[0] * values[1]] + values[2:]
    elif signs[0] == '1':
        values = [values[0] + values[1]] + values[2:]
    else:
        values = [int(str(values[0]) + str(values[1]))] + values[2:]
    return compute(values, signs[1:])
    
    
    
def tri(n, length):
    if n == 0:
        base3 = '0'
    else:
        base3 = ''
        while n > 0:
            base3 = str(n % 3) + base3
            n //= 3
    base3 = base3.zfill(length)
    
    return base3
with open('input.txt', 'r') as f:
    f = f.readlines()
   
    score = 0 
    for l in f:
        result, values = l.split(': ')
        values = [int(i) for i in values[:-1].split(' ')]
        
        for i in range(3**(len(values)-1)):
            i = list(tri(i, len(values)-1))
            
            
            if compute(values.copy(), i) == int(result):
                score += int(result)
                break
            
    print(score)