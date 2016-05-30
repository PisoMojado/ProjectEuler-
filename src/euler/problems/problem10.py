from euler.common.EratosthenesSieve import produce_prime_sum_map_under_n

prime_map = produce_prime_sum_map_under_n(1000000)
trials = int(raw_input())
for i in range(trials):
    current_N = int(raw_input())
    print(prime_map[current_N])