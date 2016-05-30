def greater_than(left, right):
    return left if left > right else right


def get_largest_product_in_number_line(number_line):
    current_product = reduce(lambda x, y: x * y, number_line[:4])
    largest_product = current_product
    for j in range(4, len(number_line)):
        # current_product /= number_line[j - 4]
        # current_product *= number_line[j]
        current_product = number_line[j] *\
                          number_line[j - 1] *\
                          number_line[j - 2] *\
                          number_line[j - 3]
        if current_product > largest_product:
            largest_product = current_product
    return largest_product


row_width = 20
col_length = row_width
number_grid = []
for i in range(col_length):
    line = raw_input().split()
    number_grid.append(map(int, line))
# we've prepped the grid. It's time to process the rows, columns, and diagonals:
# horizontals:
product = reduce(greater_than,
                 # horizontals:
                 [get_largest_product_in_number_line(number_grid[i])
                  for i in range(row_width)] +
                 # verticals:
                 [get_largest_product_in_number_line(
                                           [number_grid[j][i]
                                            for j in range(col_length)])
                  for i in range(row_width)] +
                 # backslash diagonals:
                 [get_largest_product_in_number_line(
                                           [number_grid[j][j + i]
                                            for j in range(col_length - i)])
                  for i in range(row_width - 3)] +
                 [get_largest_product_in_number_line(
                                           [number_grid[j + i][j]
                                            for j in range(row_width - i)])
                  for i in range(col_length - 3)] +
                 # forwardslash diagonals:
                 [get_largest_product_in_number_line(
                                           [number_grid[j][i - j]
                                            for j in range(i + 1)])
                  for i in range(3, row_width)] +
                 [get_largest_product_in_number_line(
                                           [number_grid[j][i + row_width - 1 - j]
                                            for j in range(i, row_width)])
                  for i in range(col_length - 3)])
print(product)
