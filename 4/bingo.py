import numpy as np

def read_draw(line):
    drawn_numbers = line.split(",") 
    drawn_numbers = list(map(int, drawn_numbers))
    return drawn_numbers


def get_line(f):
    '''Reads a line that is not empty'''
    line = f.readline().strip()
    while(line == ""):
        line = f.readline()
        if not line:
            return None
    
    return line

def get_sheet(f):
    sheet = []
    for i in range(5):

        line = get_line(f)

        if line == None:
            sheet = None
            break
        
        line = list(map(int, line.split()))
        sheet.append(line)
    
    return sheet

class BingoSheets():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(BingoSheets, cls).__new__(cls)
        
        return cls.instance
    
    def __init__(self):
        self.sheets = []

    def add_sheet(self, sheet):
        self.sheets.append(sheet)

    def __set_winning_sheet(self, index):
        self.winning_sheet = index

    def solve(self, drawn_numbers):
        for number in drawn_numbers:
            for sheet in self.sheets:
                sheet.check(number)
                if(sheet.win):
                    self.__set_winning_sheet(self.sheets.index(sheet))
                    self.winning_number = number
                    return sheet.sheet

class BingoSheet():
    def __init__(self, sheet):
        self.sheet = sheet
        self.win = False

    def __check_for_win(self):
        for row in self.sheet:
            if len(set(row)) == 1:
                self.win = True
                return

        for row in np.transpose(self.sheet):
            if len(set(row)) == 1:
                self.win = True

    def check(self, number):
        for row in self.sheet:
            if number in row:
                row[row.index(number)] = 'X'
                self.__check_for_win()
