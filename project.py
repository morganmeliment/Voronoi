precision = 100
scale = 12
grid = []
#points are formatted as [x, y]
existingpoints = [[4, 3], [9, 6], [2, 10]]
for point in range(0, precision**2):
    grid.append([(point % precision + 1) / scale, ((point - (point % precision)) / precision + 1) / scale])

def getclosestpoint(dot, trypoints):
    distances = []
    for dot2 in trypoints:
        xdiff = max(dot2[0], dot[0]) - min(dot2[0], dot[0])
        ydiff = max(dot2[1], dot[1]) - min(dot2[1], dot[1])
        distances.append([dot2, (xdiff**2 + ydiff**2)**(1/2)])
    shortest = min([num[1] for num in distances])
    for dis in distances:
        if dis[1] == shortest:
            if dis[0] == trypoints[-1]:
                return 1
            else:
                return 0

areas = []
for vector in grid:
    newpoints = existingpoints + [vector]
    thispoints = 0
    [counts[e] = 0 for e in newpoints]
    for p in grid:
        cl = getclosestpoint(p, newpoints)
        thispoints += cl
    areas.append([vector, thispoints / (precision**2)])

bestarea = max([a[1] for a in areas])
print(bestarea)













































