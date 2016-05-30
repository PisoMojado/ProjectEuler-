from euler.common.EratosthenesSieve import produce_primes_under_n

trials = int(raw_input())
# the first 10000 primes are all underneath the below constant
first_lots_of_primes = produce_primes_under_n(104730)
for i in range(trials):
    current_N = int(raw_input())
    print first_lots_of_primes[current_N - 1]
