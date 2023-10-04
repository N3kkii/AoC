def get_coords(lines):
    #getting rid of the arrow in input
    for line in lines:
        line.pop(line.index('->'))
    #merging start and stop coordinates into one array
    lines = [x[0].split(',') + x[1].split(',') for x in lines]
    #converting to ints
    for line in lines:
        lines[lines.index(line)] = list(map(int, line))
    #putting arrays with coordinates into dictionary
    keys = ['x1', 'y1', 'x2', 'y2']
    lines = [{key: value for key, value in zip(keys, sublist)} for sublist in lines]
    return lines

def get_overlaps(coords, overlaps, diagonals=False):
    for coord in coords:
        x1 = coord['x1']
        x2 = coord['x2']
        y1 = coord['y1']
        y2 = coord['y2']
        
        minx = min(x1, x2)
        miny = min(y1,y2)

        distance = (abs(x1 - x2) if y1 == y2 else abs(y1 - y2)) + 1
        if x1 == x2:
            for i in range(distance):
                if f'{x1}-{miny + i}' in overlaps:
                    overlaps[f'{x1}-{miny + i}'] += 1
                else:
                    overlaps[f'{x1}-{miny + i}'] = 1
                
        elif y1 == y2:
            for i in range(distance):
                if f'{minx + i}-{y1}' in overlaps:
                    overlaps[f'{minx + i}-{y1}'] += 1
                else:
                    overlaps[f'{minx + i}-{y1}'] = 1
        
        else:
            if diagonals:
                kx = -1 if x1 > x2 else 1
                ky = -1 if y1 > y2 else 1
                for i in range(distance):
                    if f'{x1 + i*kx}-{y1 + i*ky}' in overlaps:
                        overlaps[f'{x1 + i*kx}-{y1 + i*ky}'] += 1
                    else:
                        overlaps[f'{x1 + i*kx}-{y1 + i*ky}'] = 1