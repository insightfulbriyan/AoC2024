import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
example = False
with open("ex_input.txt" if example else "input.txt", "r") as f:
    f = [
        [tuple([int(k) for k in j[2:].split(",")]) for j in i.split(" ")]
        for i in f.read().split("\n")
    ]

    h = 11 if example else 101
    v = 7 if example else 103

    for j in range(10000):  
        grid = [[[]] * h for _ in range(v)]
        # initial
        for i in f:
            x = (i[0][0] + i[1][0] * j) % h
            y = (i[0][1] + i[1][1] * j) % v
            grid[y][x] = grid[y][x] + [i]

        plt.figure(figsize=(v,h))
        # plt.imshow([[len(k)==0 for k in i] for i in grid], cmap='gray', interpolation='none')
        plt.axis('off')  # Turn off the axis numbers and ticks
        # Optionally, save the image to a file
        plt.imsave('img/bw_image' + str(j) + '.png', [[len(k)==0 for k in i] for i in grid], cmap='gray')
        
