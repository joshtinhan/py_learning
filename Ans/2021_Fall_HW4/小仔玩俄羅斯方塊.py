height = int(input())
width = int(input())
matrix = [[] for i in range(height)]
for i in range(width):
    for j in range(len(matrix)):
        matrix[i].append("Ｏ")


class All_type:
    all = []

    def __init__(self, shape, initial, pos=[]):
        self.shape = shape
        self.pos = pos
        self.initial = initial
        if shape == "I":
            print(self.initial)
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
        init_x = 0
        for i in steps_arr:
            # print(i)
            if i == "left":
                if self.can_move(i, matrix):
                    init_x -= 1
            if i == "right":
                if self.can_move(i, matrix):
                    init_x += 1
        for i in self.pos:
            i[1] = i[1] + init_x

    def can_move(self, direction, matrix):
        leftest, rightest = self.get_leftest_and_rightest(self.shape)
        if direction == "left":
            for i in self.pos:
                if matrix[i[0]][i[1]-1] == "*" or leftest - 1 < 0:
                    print("error")
                    return False
        elif direction == "right":
            for i in self.pos:
                if matrix[i[0]][i[1]+1] == "*" or rightest + 1 >= width:
                    return False
        return True

    def can_drop(self, matrix):
        for i in self.pos:
            if matrix[i[0]+1][i[1]] == "*" or i[0] == height - 1:
                return False
        return True

    def dropping(self, matrix):
        if self.can_drop(matrix):
            for i in self.pos:
                i[0] = i[0]+1
            return True
        return False

    def __repr__(self):
        return f"All_type({self.shape},{self.pos})"


All_type("I", 1)
All_type("I", 0)
All_type("I", 2)
All_type("I", 3)
# arr = ["left", "left", "right"]
arr = []

for i in All_type.all:
    i.dropping(matrix)
    i.move(arr, matrix)
    for j in i.pos:
        matrix[j[0]][j[1]] = "*"
print(All_type.all)
print(matrix)
