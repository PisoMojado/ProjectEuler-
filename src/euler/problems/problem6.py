def squared_sum_diff(n):
    return (3 * n ** 4 + 2 * n ** 3 - 3 * n ** 2 - 2 * n) / 12


trials = int(raw_input())
for i in range(trials):
    current_N = int(raw_input())
    print(squared_sum_diff(current_N))
