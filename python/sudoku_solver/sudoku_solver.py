# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

class SudokuBoard:

    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.score = [[0 for _ in range(9)] for _ in range(9)]
        self.perms = [[list() for _ in range(9)] for _ in range(9)]
    
    def __repr__(self):
        ret = ''
        for n, row in enumerate(self.board):
            for m, val in enumerate(row):
                if not val or val < 1:
                    ret += '. '
                else:
                    ret += str(val) + ' '
                if not (m+1)%3 and m != 8:
                    ret += '|'
            ret += '\n'
            if not (n+1)%3 and n != 8:
                ret += '-'*18 + '\n'

        return ret

    def change_board_value(self, x, y, val):
        try:
            val = int(val)
        except ValueError:
            val = 0
        self.board[y][x] = val

    def change_board_permutations(self, x, y, arr):
        self.perms[y][x] = arr


    def __get_row(self, y, arr):
        if y < 0 or y > 9:
            return []
        return list(arr[y])

    def __get_col(self, x, arr):
        if x < 0 or x > 9:
            return []
        r = []
        for i in range(9):
            r.append(arr[i][x])
        return r
    
    def __get_cell(self, m, n, arr):
        r = []
        for i in range(n*3, n*3 + 3):
            for j in range(m*3, m*3 + 3):
                r.append(self.board[i][j])
        return r
        
    def vals_get_value(self, x, y):
        return self.board[y][x]

    def vals_get_row(self, y):
        return self.__get_row(y, self.board)

    def vals_get_col(self, x):
        return self.__get_col(x, self.board)
    
    def vals_get_cell(self, m, n):
        return self.__get_cell(m, n, self.board)
    
    def vals_get_cell_xy(self, x, y):
        return self.vals_get_cell(x//3, y//3)


    def perms_get_row(self, y):
        return self.__get_row(y, self.perms)

    def perms_get_col(self, x):
        return self.__get_col(x, self.perms)
    
    def perms_get_cell(self, m, n):
        return self.__get_cell(m, n, self.perms)
    
    def perms_get_cell_xy(self, x, y):
        return self.perms_get_cell(x//3, y//3)

    def check(self):
        for n in range(9):
            for m in range(9):
                val = self.vals_get_value(n, m)
                if not val or val =='0':
                    return False
                col = self.vals_get_col(m)
                row = self.vals_get_row(n)
                cel = self.vals_get_cell_xy(m, n)

                col.pop(m)
                row.pop(n)
                cel.pop((n//3)*3 + (m//3))

    def calc_perms(self):
        for i in range(9):
            for j in range(9):
                col = self.vals_get_col(i)
                row = self.vals_get_row(j)
                cel = self.vals_get_cell_xy(i, j)
                self.change_board_permutations(i, j, SudokuBoard.s_get_perms(col + row + cel))
                if self.vals_get_value(i, j):
                    continue

    def clone(self):
        c = SudokuBoard()
        c.board = self.board
        c.score = self.score
        c.perms = self.perms
        return c

    @staticmethod
    def s_get_perms(arr):
        defaults = list(range(1,10))
        r = []
        for i in defaults:
            if i not in arr:
                r.append(i)
        return r

def s_remove_dupes(arr):
    r = []
    for i in arr:
        if i not in r:
            r.append(i)
    return r

def padstr(text, padding):
    if not isinstance(text, str):
        text = str(text)
    if len(text) > padding:
        return text
    return text + ' '*(padding - len(text))

def print_perms(board: SudokuBoard):
    longest = 0
    for i in range(9):
        for j in range(9):
             x = len(board.perms[j][i])
             if x > longest:
                longest = x

    for i in range(9):
        for j in range(9):
             item = board.perms[i][j]
             text = ''.join([str(i) for i in item])
             if not item:
                text = '[.]'
             print(padstr(text, longest), end=' ')
        print()


if __name__ == '__main__':
    b = SudokuBoard()
    
    for n, i in enumerate(board):
        for m, j in enumerate(i):
            b.change_board_value(m, n, j)

    
    print('before', b, sep='\n')

    for _ in range(10):

        calc_perms(b)    
        for x in range(9):
            for y in range(9):
                val = b.perms[y][x]
                if len(val) == 1:
                    b.change_board_value(x, y, val[0])
    
    
    
    
    print('after', b, sep='\n')
    print_perms(b)



