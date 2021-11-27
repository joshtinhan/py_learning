matrix = [[0 for i in range(5)] for j in range(5)]


def findNextCellToFill(grid, i, j):
    for x in range(i, 5):
        for y in range(j, 5):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 5):
        for y in range(0, 5):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def check_Index(i, j, irregular_area):
    for index, irregular_area_pos in enumerate(irregular_area):
        if (str(i), str(j)) in irregular_area_pos:
            return index


def isValid(grid, i, j, e, irregular_area_pos):
    rowOk = all([e != grid[i][x] for x in range(5)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(5)])
        if columnOk:
            for irregular_area_pos in irregular_area[check_Index(i, j, irregular_area)]:
                area_pos_X, area_pos_Y = irregular_area_pos
                if grid[int(area_pos_X)][int(area_pos_Y)] == e:
                    return False
            return True
    return False


def solveSudoku(grid, irregular_area_pos, i=0, j=0):
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1, 6):
        if isValid(grid, i, j, e, irregular_area_pos):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


irregular_area = [[] for i in range(5)]
for i in range(5):
    area = input().split()
    for j in area:
        x, y = j.split(",")
        irregular_area[i].append((x, y))
while True:
    try:
        pos, value = [v for v in input().split()]
        x, y = pos.split(",")
        matrix[int(x)][int(y)] = int(value)

    except EOFError:
        solveSudoku(matrix, irregular_area)
        if any(0 in sublist for sublist in matrix):
            print("no solution!")
        else:
            for j in matrix:
                print(" ".join(str(v) for v in j))
        break


# 0,1 1
# 0,3 5
# 1,2 5
# 3,2 2
# 4,1 4
# 4,3 2
# 0,0 0,1 2,0 3,0 1,0
# 0,2 1,1 1,2 2,1 2,2
# 0,3 0,4 1,3 1,4 2,3
# 2,4 3,3 3,2 3,4 3,1
# 4,0 4,1 4,4 4,2 4,3
