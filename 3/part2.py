def get_o2_rating(numbers):
    index = 0
    lines = numbers
    
    while len(lines) != 1:
        ones = 0
        zeros = 0

        for line in lines:
            if line[index % len(line)] == '1':
                ones += 1
            elif line[index % len(line)] == '0':
                zeros += 1
        
        if ones > zeros or ones == zeros:
            lines = list(filter(lambda x: x[index % len(line)] == '1', lines))

        else:
            lines = list(filter(lambda x: x[index % len(line)] =='0', lines))

        index += 1

    return int(lines[0], 2)       

def get_co2_rating(numbers):
    index = 0
    lines = numbers

    while len(lines) != 1:
        ones = 0
        zeros = 0
        for line in lines:
            if line[index % len(line)] == '1':
                ones += 1
            elif line[index % len(line)] == '0':
                zeros += 1
        
        if zeros < ones or ones == zeros:
            lines = list(filter(lambda x: x[index % len(line)] == '0', lines))

        else:
            lines = list(filter(lambda x: x[index % len(line)] == '1', lines))

        index += 1

    return int(lines[0], 2)       

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
        life_support = get_o2_rating(lines) * get_co2_rating(lines)
        print(life_support)
            