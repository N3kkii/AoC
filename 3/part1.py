if __name__ == '__main__':

    num_of_bits = 12

    ones = [0] * num_of_bits
    zeros = [0] * num_of_bits

    with open("input.txt", "r") as f:
        for line in f:
            for i in range(num_of_bits):
                if line[i] == '1':
                    ones[i] += 1
                
                else:
                    zeros[i] += 1

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(num_of_bits):
        if ones[i] > zeros[i]:
            gamma_rate += '1'
            epsilon_rate += '0'

        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
