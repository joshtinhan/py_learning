

class All_type:
    all = []

    def __init__(self, shape, initial, pos=[]):
        self.shape = shape
        self.pos = pos
        self.initial = initial
        if shape == "I":
            each_pos = []
            for i in range(4):
                each_pos.append([i, self.initial])
            self.pos = each_pos
        if shape == "J":
            each_pos = []
            for i in range(3):
                each_pos.append([i, initial+1])
            each_pos.append([2, initial])
            self.pos = each_pos
        if shape == "L":
            each_pos = []
            for i in range(3):
                each_pos.append([i, initial])
            each_pos.append([2, initial+1])
            self.pos = each_pos
        if shape == "O":
            each_pos = []
            for i in range(2):
                each_pos.append([i, initial])
                each_pos.append([i, initial+1])
            self.pos = each_pos
        if shape == "S":
            each_pos = []
            for i in range(2):
                each_pos.append([0, initial+1+i])
                each_pos.append([1, initial+i])
            self.pos = each_pos
        if shape == "T":
            each_pos = []
            for i in range(3):
                each_pos.append([0, initial+i])
            each_pos.append([1, initial+1])
            self.pos = each_pos
        if shape == "Z":
            each_pos = []
            for i in range(2):
                each_pos.append([0, initial+i])
                each_pos.append([1, initial+1+i])
            self.pos = each_pos
        All_type.all.append(self)

    def get_leftest_and_rightest(self, shape):
        if shape == "I":
            leftest = self.initial
            rightest = self.initial
        if shape == "J" or shape == "L" or shape == "O":
            leftest = self.initial
            rightest = self.initial+1
        if shape == "S" or shape == "T" or shape == "Z":
            leftest = self.initial
            rightest = self.initial+2
        return leftest, rightest

    def move(self, steps_arr, matrix):
        for i in steps_arr:
            if i == "left":
                if self.can_move(i, matrix):
                    self.pos = list(map((lambda x: [x[0], x[1]-1]), self.pos))
            if i == "right":
                if self.can_move(i, matrix):
                    self.pos = list(map((lambda x: [x[0], x[1]+1]), self.pos))

    def can_move(self, direction, matrix):
        leftest, rightest = self.get_leftest_and_rightest(self.shape)
        if direction == "left":
            for i in self.pos:
                if i[1] < 1:
                    return False
                if matrix[i[0]][i[1]-1] == "＊" or leftest - 1 < 0:
                    return False
        elif direction == "right":
            for i in self.pos:
                if i[1] >= width-1:
                    return False
                if matrix[i[0]][i[1]+1] == "＊" or rightest + 1 >= width:
                    return False
        return True

    def can_drop(self, matrix):
        for i in self.pos:
            try:
                if i[0] >= height-1:
                    return False
                if matrix[i[0]+1][i[1]] == "＊" or i[0] == height - 1:
                    return False
            except IndexError:
                return False
        return True

    def dropping(self, matrix):
        if self.can_drop(matrix):
            # for i in self.pos:
            #     i[0] = i[0]+1
            self.pos = list(map((lambda x: [x[0]+1, x[1]]), self.pos))
            if self.dropping(matrix):
                return True
        return False

    def eliminate(self, matrix):
        get_eliminated = ["＊"]*width
        get_added = ["Ｏ"]*width
        for i in matrix:
            if i == get_eliminated:
                matrix.remove(i)
                matrix.insert(0, get_added)

    def __repr__(self):
        return f"All_type({self.shape},{self.pos})"


# All_type("I", 1)
# All_type("I", 0)
# All_type("I", 2)
# All_type("I", 3)
# All_type("T", 1)
# All_type("O", 1)
# arr = []

# All_type("I", 3)
# All_type("T", 0)
# arr = [["left", "left", "right"], ["right"]]

# All_type("O", 1)
# All_type("T", 0)
# arr = [[], ["right"]]

width = int(input())
height = int(input())
matrix = [[] for i in range(height)]
for i in range(width):
    for j in matrix:
        j.append("Ｏ")
string = ""
while True:
    try:
        game_start = [v for v in input().split()]
        type = game_start[0]
        init_move = game_start[1]
        move_array = game_start[2:]
        v = All_type(type, int(init_move))
        v.dropping(matrix)
        v.move(move_array, matrix)
        for j in v.pos:
            if j[0] > height-1 or j[1] > width-1 or matrix[j[0]][j[1]] == "＊":
                string = "Game Over!"
                print(string)
                break

            matrix[j[0]][j[1]] = "＊"
            v.eliminate(matrix)

    except EOFError:
        if not string:
            for i in matrix:
                print("".join(j for j in i))
        break

# print(All_type.all)
