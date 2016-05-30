num_count = int(raw_input())
sum = 0
for i in range(num_count):
    sum += int(raw_input()[:12])
print str(sum)[:10]
