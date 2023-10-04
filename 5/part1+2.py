from coords import *

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = [line.split() for line in f.readlines()]
        coords = get_coords(lines)

        overlaps = {}
        get_overlaps(coords, overlaps)
        part1 = 0

        for key, value in overlaps.items():
            if value >= 2:
                part1 += 1

        overlaps = {}
        get_overlaps(coords, overlaps, True)
        part2 = 0
        

        for key, value in overlaps.items():
            if value >= 2:
                part2 += 1

        print(f'part1: {part1}, part2: {part2}')