def read_draw(f):
    drawn_numbers = f.readline().split(",")
    
    drawn_numbers.pop() #removing newline
    f.readline() #skipping empty line

    return drawn_numbers

#class Bingosheet:
#    def __init__(self, ):


if __name__ == '__main__':

    with open("input.txt", "r") as f:
        drawn_numbers = read_draw(f)
        line = f.readline().strip().split(" ")
        print(line)
