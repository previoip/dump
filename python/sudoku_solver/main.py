from sudoku_solver import SudokuBoard
import csv

def sudoku_loader(csvPath: str, limit=0):
    with open(csvPath) as fp:
        reader = csv.reader(fp)
        data = []
        idx = 0
        while True:
            try:
                data.append(next(reader))
            except StopIteration:
                break
            idx += 1
            if idx >= limit:
                break
    return data
    

if __name__ == '__main__':
    csvPath = './python/sudoku_solver/sudoku.csv'
    data = sudoku_loader(csvPath, 5)
    print(data)