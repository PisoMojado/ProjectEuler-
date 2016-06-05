from euler.common.BinomialCoefficients import binomial

large_divisor = 1000000007
trial_count = int(raw_input())
for i in range(trial_count):
    values = map(int, raw_input().split())
    print binomial(sum(values), values[0]) % large_divisor
