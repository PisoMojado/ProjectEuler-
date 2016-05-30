from euler.common.Fibonacci import FibonacciSeries

trials = int(raw_input())
for i in range(trials):
    ceiling = int(raw_input())
    fib_series = FibonacciSeries(ceiling)
    print sum(num for num in fib_series if num % 2 == 0)
