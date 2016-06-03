def get_collatz_cycle_count(n):
    cycle_count = 1
    while n > 1:
        if n % 2:
            n = n + n - (n >> 1)
            cycle_count += 2
        else:
            n >>= 1
            cycle_count += 1
    return cycle_count


def get_collatz_map_under_n(n):
    collatz_map = {}
    for i in range(1, n+1):
        cycle_count = 1
        temp = i
        while temp > 1:
            if temp in collatz_map:
                cycle_count += collatz_map[temp] - 1
                break
            elif temp % 2:
                temp = temp + temp - (temp >> 1)
                cycle_count += 2
            else:
                temp >>= 1
                cycle_count += 1
        collatz_map[i] = cycle_count
    return collatz_map

