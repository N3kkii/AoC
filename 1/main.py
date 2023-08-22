if __name__ == '__main__':
    increases = 0

    try:
        with open("input.txt", "r") as input_file:
            lines = input_file.readlines()
            
            first = int(lines[0])
            second = int(lines[1])
            third = int(lines[2])
            prev_measure = first + second + third

            for current_index in range(len(lines) - 2):
                
                first = int(lines[current_index + 0])
                second = int(lines[current_index + 1])
                third = int(lines[current_index + 2])

                curr_measure = first + second + third
                print("Comparing: " + str(curr_measure) + " and " + str(prev_measure))
                if curr_measure > prev_measure:
                    increases += 1

                prev_measure = curr_measure

    except:
        raise NameError("Error opening file")

    finally:
        print(increases)
