precision = 60
scale = 12
grid = []
#points are formatted as [x, y]
existingpoints = [[4, 3], [9, 6], [2, 10]]
for point in range(0, precision**2 + precision):
    grid.append([(point % precision) * (scale / precision), ((point - (point % precision)) / precision) * (scale / precision)])

def getclosestpoint(dot, trypoints, po):
    distances = []
    for dot2 in trypoints:
        xdiff = max(dot2[0], dot[0]) - min(dot2[0], dot[0])
        ydiff = max(dot2[1], dot[1]) - min(dot2[1], dot[1])
        distances.append([dot2, (xdiff**2 + ydiff**2)**(1/2)])
    shortest = min([num[1] for num in distances])
    for dis in distances:
        if dis[1] == shortest:
            if dis[0] == po:
                return 1
            else:
                return 0

areas = []
for vector in grid:
    newpoints = existingpoints + [vector]
    thispoints = 0
    for p in grid:
        cl = getclosestpoint(p, newpoints, vector)
        thispoints += cl
    areas.append([vector, (thispoints / (precision**2))])

bestarea = max([a[1] for a in areas])
for r in areas:
    if r[1] == bestarea:
        print(r)













































