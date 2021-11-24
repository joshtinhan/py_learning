matrix = [[0 for i in range(5)] for j in range(5)]

irregular_area = []
for i in range(5):
    area = input().split()
    for j in area:
        every_cell = j.split(",")
        irregular_area.append(every_cell)
# print(irregular_area)


def findNextCellToFill(matrix, i, j):
    for x in range(i, 5):
        for y in range(j, 5):
            if matrix[x][y] == 0:
                return x, y
    for x in range(0, 5):
        for y in range(0, 5):
            if matrix[x][y] == 0:
                return x, y
    return -1, -1


def isValid(matrix, i, j, e):
    rowOk = all([e != matrix[i][x] for x in range(5)])
    if rowOk:
        columnOk = all([e != matrix[x][j] for x in range(5)])
        if columnOk:
            for irregular_area_pos in irregular_area:
                area_pos_X, area_pos_Y = irregular_area_pos
                if matrix[int(area_pos_X)][int(area_pos_Y)] == e:
                    return False
            return True
    return False


def solveSudoku(grid, i=0, j=0):
    print(grid)
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 6):
        if isValid(grid, i, j, e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


while True:
    try:
        pos, value = [v for v in input().split()]
        x, y = pos.split(",")
        matrix[int(x)][int(y)] = int(value)
    except EOFError:
        print("exec")
        solveSudoku(matrix)
        # print(matrix)
# 0,0 0,1 2,0 3,0 1,0
# 0,2 1,1 1,2 2,1 2,2
# 0,3 0,4 1,3 1,4 2,3
# 2,4 3,3 3,2 3,4 3,1
# 4,0 4,1 4,4 4,2 4,3
