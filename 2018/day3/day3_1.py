claims = [[0 for x in range(1000)] for y in range(1000)]
count = 0
with open('../inputs/day3.txt') as f:
    for line in f:
        strippedLine = line.strip()
        coords = strippedLine.split('@')[1]
        x = int(coords.split(':')[0].split(',')[0])
        y = int(coords.split(':')[0].split(',')[1])
        width = int(coords.split(':')[1].split('x')[0])
        height = int(coords.split(':')[1].split('x')[1])
        for i in range(x, x+width):
            for j in range(y, y+height):
                claims[i][j] += 1
                if claims[i][j] == 2:
                    count += 1

print(count)
