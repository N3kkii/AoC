import numpy as np
from bingo1 import *

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        drawn_numbers = read_draw(get_line(f))
        bingosheets = BingoSheets()

        sheet = get_sheet(f)
        while (sheet):
            bingosheets.add_sheet(BingoSheet(sheet))
            sheet = get_sheet(f)

        sheet = bingosheets.solve(drawn_numbers)
        result = 0
        for row in sheet:
            for i in row:
                if type(i) == int:
                    result += i

        print(f"Final result: {result * bingosheets.winning_number}")
