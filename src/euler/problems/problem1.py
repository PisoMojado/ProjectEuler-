trials = int(raw_input())
for i in range(trials):
    ceiling = int(raw_input())
    last_num = ceiling - 1
    three_count = last_num / 3
    five_count = last_num / 5
    fifteen_count = last_num / 15
    solution = 3 * (three_count * (three_count + 1) / 2) \
               + 5 * (five_count * (five_count + 1) / 2) \
               - 15 * (fifteen_count * (fifteen_count + 1) / 2)
    print(solution)
