import random


def read_sudoku(filename):
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def group(values, n):
    l = [values[i:i+n] for i in range(0, len(values), n)]
    return l


def display(values):
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def get_row(values, pos):
    row, col = pos
    return values[row]


def get_col(values, pos):
    row, col = pos
    return [values[i][col] for i in range(len(values))]


def get_block(values, pos):
    row, col = pos
    row = (row // 3) * 3
    col = (col // 3) * 3
    return [values[row+i][col+j] for i in range(3) for j in range(3)]


def find_empty_positions(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                return (i, j)


def find_possible_values(grid, pos):
    num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    row = get_row(grid, pos)
    col = get_col(grid, pos)
    block = get_block(grid, pos)
    for item in row:
        if (item != '.') and (item in num_set):
            num_set.remove(item)
    for item in col:
        if (item != '.') and (item in num_set):
            num_set.remove(item)
    for item in block:
        if (item != '.') and (item in num_set):
            num_set.remove(item)
    return num_set


def solve(grid):
    pos = find_empty_positions(grid) #находим свободную позицию
    if not pos:
        return grid # если свободных позиций не осталось, то выводим решение
    row, col = pos # записываем значения строки и столбца в row и col соответственно
    num_set = find_possible_values(grid, pos) # находим все возможные значения для ячейки
    for item in num_set: # для каждого возможного значения
        grid[row][col] = item  # записываем его в ячейку
        solution = solve(grid) # продолжаем решать судоку
        if solution:
            return solution # если свободных позиций не осталось, то возвращаем решение
    grid[row][col] = '.'


def check_solution(solution):
    num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    for i in range(len(solution)):
        row_set = set(get_row(solution, (i, 0)))
        if row_set != num_set:
            return False

    for i in range(len(solution)):
        col_set = set(get_col(solution, (0, i)))
        if col_set != num_set:
            return False

    for i in range(0, len(solution), 3):
        for j in range(0, len(solution), 3):
            block_set = set(get_block(solution, (i, j)))
            if block_set != num_set:
                return False
    return True


def generate_sudoku(N):
    grid = solve([['.' for i in range(9)] for j in range(9)])
    if N >= 81:
        N = 0
    else:
        N = 81 - N
    while N != 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != '.':
            grid[row][col] = '.'
            N -= 1
    return grid


grid = read_sudoku('puzzle3.txt')
display(grid)
#grid = read_sudoku('puzzle.txt')
#display(grid)
#print(get_block(grid, (4, 7)))
#print(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]))
#print(find_possible_values(grid, (0, 2)))
solution = solve(grid)
display(solution)
print(check_solution(solution))
sudoku = generate_sudoku(40)
display(sudoku)
print(sum(1 for row in sudoku for e in row if e == '.'))