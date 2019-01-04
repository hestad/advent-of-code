claims = [[[] for x in range(1000)] for y in range(1000)]
ids = set()
count = 0
with open('../inputs/day3.txt') as f:
    # 1267 @ 274,570: 20x10
    for line in f:
        strippedLine = line.strip()
        id = int(strippedLine.split('@')[0].strip('#').strip())
        ids.add(id)
        coords = strippedLine.split('@')[1]
        x = int(coords.split(':')[0].split(',')[0])
        y = int(coords.split(':')[0].split(',')[1])
        width = int(coords.split(':')[1].split('x')[0])
        height = int(coords.split(':')[1].split('x')[1])
        for i in range(x, x+width):
            for j in range(y, y+height):
                claims[i][j].append(id)

for outer in claims:
    for element in outer:
        if len(element) > 1:
            for id in element: ids.discard(id)

print(ids)