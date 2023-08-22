pos = 0
depth = 0
aim = 0

with open("input.txt", "r") as f:
    for line in f:
        inst = line.split()
        direction = inst[0]
        units = int(inst[1])

        match direction:
            case "forward":
                pos += units
                depth += aim * units
            
            case "down":
                aim += units

            case "up":
                aim -= units

print(pos * depth)
