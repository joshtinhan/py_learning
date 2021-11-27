empty_array = []
ans = True
sudoku = dict()
for i in range(9):
    for j in range(9):
        sudoku[str(j)+str(i)] = empty_array[i][j]


def create_arr(x, x_to, y, y_to):
    arr = []
    for i in range(x, x_to+1):
        for j in range(y, y_to+1):
            arr.append(sudoku[str(i)+str(j)])
    return arr


def is_legal(arr):
    count_zero = arr.count(0)
    count_not_zero = int()
    for i in range(1, 10):
        if arr.count(i) > 1:
            return False
        elif arr.count(i) == 1:
            count_not_zero += 1
    if count_not_zero+count_zero == 9:
        return True
    else:
        return False


for i in range(9):
    if is_legal(create_arr(0, 8, i, i)) == False or is_legal(create_arr(i, i, 0, 8)) == False:
        ans = False
for i in range(0, 9, 3):
    if is_legal(create_arr(i, int(i)+2, 0, 2)) == False or is_legal(create_arr(i, int(i)+2, 3, 5)) == False or is_legal(create_arr(i, int(i)+2, 6, 8)) == False:
        ans = False
print(bool(ans))
