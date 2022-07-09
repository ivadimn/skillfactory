class Field:
    def __init__(self, size):
        self.size = size
        self.min_rating = 0
        self.max_rating = 0
        self.field = [0 for _ in range(size * size)]
        self.obhod = [[0 for _ in range(size)] for _ in range(size * 2 + 2)]
        self.create_obhod()

    def create_obhod(self):
        obhod_len = len(self.obhod)
        for i in range(self.size):
            for j in range(self.size):
                self.obhod[i][j] = j + (i * self.size)
                self.obhod[i + num][j] = i + (j * self.size)

        for j in range(self.size):
            self.obhod[obhod_len - 1][j] = j * (self.size + 1)
            self.obhod[obhod_len - 2][j] = (self.size - 1) * (j + 1)

        self.obhod.reverse()


    def answer(self):
        if self.field[(len(self.field) - 1) // 2] == 0:
            self.set_value((self.size - 1) // 2, (self.size - 1) // 2, -1)
            return

        min_pos = self.get_min_rating()
        max_pos = self.get_max_rating()
        if self.max_rating > self.min_rating:
            self.set_on_pos(max_pos, -1)
        else:
            self.set_on_pos(min_pos, -1)


    def printField(self):
        print("   |", end = "")
        for i in range(self.size):
            print("_{0}_|".format(i), end = "")
        print()
        row = 0
        for i in range(0, len(self.field), self.size):
            print("_{0}_|".format(row), end = "")
            row += 1
            for j in range(i, i + self.size):
                if self.field[j] == 1:
                    val = "x"
                elif self.field[j] == -1:
                    val = "0"
                else:
                    val = " "
                print("_{0}_|".format(val), end = "")
            print()
        print()

    def get_max_rating(self):
        self.max_rating = -self.size
        pos = 0
        for i, line in enumerate(self.obhod):
            raiting = self.summa(line, -self.size)
            if raiting > self.max_rating:
                self.max_rating = raiting
                pos = i
        return pos

    def get_min_rating(self):
        self.min_rating = self.size
        pos = 0
        for i, line in enumerate(self.obhod):
            raiting = self.summa(line, self.size)
            if raiting < self.min_rating:
                self.min_rating = raiting
                pos = i
        return pos

    def set_on_pos(self, pos, val):
        for elem in self.obhod[pos]:
            if self.field[elem] == 0:
                self.field[elem] = val
                break

    def set_value(self, i, j, val):
        self.field[i * self.size + j] = val


    def is_fill(self):
        for elem in self.field:
            if elem == 0:
                return False
        return True

    def is_win(self):
        for obhod in self.obhod:
            s = 0
            for elem in obhod:
                s += self.field[elem]
            if s == self.size or s == (-self.size):
                return True
        return False

    def summa(self, lst: list, default):
        if all([self.field[elem] != 0 for elem in lst]):
            return default
        s = 0
        for elem in lst:
            s += self.field[elem]
        return s

num = 3
field = Field(num)
while not field.is_fill() and (not field.is_win()):
    val = list(map(int, input("Введите через пробел Строку, Столбец, Значение (1-'X'): ").split()))
    field.set_value(val[0], val[1], 1)
    print("-" * 40)
    field.answer()
    field.printField()

print("Finish")
