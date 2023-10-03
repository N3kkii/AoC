import bingo2 as b

if __name__ == '__main__':
    with open("input.txt", "r") as f:
        drawn_numbers = b.read_draw(b.get_line(f))
        bingosheets = b.BingoSheets()

        sheet = b.get_sheet(f)
        while (sheet):
            bingosheets.add_sheet(b.BingoSheet(sheet))
            sheet = b.get_sheet(f)

        bingosheets.count_sheets()
        bingosheets.solve(drawn_numbers)
        sheet=bingosheets.sheets[bingosheets.winning_sheet].sheet
        result = 0
        for row in sheet:
            for i in row:
                if type(i) == int:
                    result += i

        print(f"Final result: {result * bingosheets.winning_number}")