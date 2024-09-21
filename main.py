
class map :
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[0 for x in range(width)] for y in range(height)]

    def set(self, x, y, value):
        self.data[y][x] = value

    def get(self, x, y):
        return self.data[y][x]

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.data[y][x], end='')
            print()

    def load(self, filename):
        with open(filename, 'r') as f:
            for y, line in enumerate(f):
                for x, c in enumerate(line):
                    if c == '.':
                        self.set(x, y, 0)
                    elif c == '#':
                        self.set(x, y, 1)