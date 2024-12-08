def compute(values, signs):
    if not signs:
        return values[0]
    elif signs[0] == '1':
        values = [values[0] * values[1]] + values[2:]
    else:
        values = [values[0] + values[1]] + values[2:]
    return compute(values, signs[1:])
    
with open('input.txt', 'r') as f:
    f = f.readlines()
   
    score = 0 
    for l in f:
        result, values = l.split(': ')
        values = [int(i) for i in values[:-1].split(' ')]
        
        for i in range(2**(len(values)-1)):
            i = list(('{0:0' + str(len(values) - 1) + 'b}').format(i))
            print(i)
            
            if compute(values.copy(), i) == int(result):
                score += int(result)
                break
        
            print(compute(values.copy(), i), result, compute(values.copy(), i) == int(result))
    print(score)