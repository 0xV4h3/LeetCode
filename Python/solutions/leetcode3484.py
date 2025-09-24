# 3484. Design Spreadsheet

class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {chr(i) : [0] * rows for i in range(65, 91)}

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell[0]][int(cell[1:]) - 1] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell[0]][int(cell[1:]) - 1] = 0

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        x = self.sheet[x[0]][int(x[1:]) - 1] if x[0].isalpha() else int(x)
        y = self.sheet[y[0]][int(y[1:]) - 1] if y[0].isalpha() else int(y)
        return x + y

if __name__ == "__main__":
    spreadsheet = Spreadsheet(3)
    print(spreadsheet.getValue("=5+7")) # 12(5 + 7)
    spreadsheet.setCell("A1", 10)
    print(spreadsheet.getValue("=A1+6")) # 16(10 + 6)
    spreadsheet.setCell("B2", 15)
    print(spreadsheet.getValue("=A1+B2")) # 25(10 + 15)
    spreadsheet.resetCell("A1")
    print(spreadsheet.getValue("=A1+B2")) # 15(0 + 15)