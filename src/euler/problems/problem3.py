from euler.common.Factors import get_largest_prime_factor

trials = int(raw_input())
for i in range(trials):
    print get_largest_prime_factor(int(raw_input()))
