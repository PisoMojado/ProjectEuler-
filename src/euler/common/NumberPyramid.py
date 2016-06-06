def _check_rows(rows):
    is_valid = True
    for i in range(0, len(rows)):
        if len(rows[i]) != i + 1:
            is_valid = False
            break
    return is_valid


class NumberPyramid(object):
    def __init__(self):
        self.rows = []

    def __init__(self, rows):
        if _check_rows(rows):
            self.rows = rows
        else:
            raise IndexError("Rows do not form a triangle")

    def __str__(self):
        return reduce(lambda a, b: a + '\n' + b,
                      [reduce(lambda x, y: x + " " + y, map(str, self.rows[i])) for i in range(len(self.rows))])

    def __repr__(self):
        return str(self.rows)

    def get_downward_neighbors(self, row, col):
        if row < 0:
            raise ValueError("Negative row numbers not allowed")
        if row < len(self.rows) - 1:
            neighbors = [self.rows[row + 1][col], self.rows[row + 1][col + 1]]
        else:
            neighbors = []
        return neighbors

    def get_upward_neighbors(self, row, col):
        if row >= len(self.rows):
            raise ValueError("Cannot ask for more than ")
        if row == 0:
            neighbors = []
        else:
            neighbors = [self.rows[row - 1][col - 1]]
            if col < len(self.rows[row - 1]):
                neighbors.append(self.rows[row - 1][col])
        return neighbors
