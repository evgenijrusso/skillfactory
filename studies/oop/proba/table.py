class Table:
    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols
        self.table = [[0] * cols for _ in range(rows)]


    def get_value(self, row, col):  #
        return (self.table[row][col] if 0 < row < self.rows and 0 < col < self.cols else None)

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

t = Table(rows=3, cols=4)
print('get rows', t.n_rows())
print('get cols', t.n_cols())
print('get value', t.get_value(2,2))