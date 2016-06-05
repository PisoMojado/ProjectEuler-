#this problem is super lame. should not be a problem this late
trial_count = int(raw_input())
for i in range(trial_count):
    n = int(raw_input())
    print sum(map(int, list(str((1 << n)))))
