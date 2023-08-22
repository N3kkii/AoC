pos = 0
depth = 0

with open("input.txt", "r") as f:
    for line in f:
        inst = line.split()
        direction = inst[0]
        units = int(inst[1])

        match direction:
            case "forward":
                pos += units
            
            case "down":
                depth += units

            case "up":
                depth -= units

print(pos * depth)
