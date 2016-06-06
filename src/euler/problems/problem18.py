from euler.common.NumberPyramid import NumberPyramid


def calc_sums(pyramid, current_sum, row, col):
    next_items = pyramid.get_downward_neighbors(row, col)
    if len(next_items) < 1:
        sums = [current_sum]
    else:
        sums = []
        index = 0
        for item in next_items:
            sums.extend(calc_sums(pyramid, current_sum + item, row + 1, col + index))
            index += 1
    return sums

trial_count = int(raw_input())
for i in range(trial_count):
    tri_size = int(raw_input())
    rows = []
    for j in range(tri_size):
        rows.append(map(int, raw_input().split()))
    pyramid = NumberPyramid(rows)
    print reduce(max, calc_sums(pyramid, pyramid.rows[0][0], 0, 0))
