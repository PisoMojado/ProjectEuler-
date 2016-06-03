#This problem took more ad-hoc optimization than is suitable for placing in our commons, but we have a Collatz module

collatz_cycle_list = [1]
largest_cycler_map = {1: 1}
trial_count = int(raw_input())
for i in range(trial_count):
    current_num = int(raw_input())
    big_cycler_under_num = 1
    if current_num in largest_cycler_map:
        big_cycler_under_num = largest_cycler_map[current_num]
    else:
        big_cycler_under_num = largest_cycler_map[len(collatz_cycle_list)]
        big_cycle_count = collatz_cycle_list[big_cycler_under_num - 1]
        for j in range(len(collatz_cycle_list) + 1, current_num + 1):
            cycle_count = 1
            temp = j
            while temp > 1:
                if temp <= len(collatz_cycle_list):
                    cycle_count += collatz_cycle_list[temp - 1] - 1
                    break
                elif temp % 2:
                    temp = temp + temp - (temp >> 1)
                    cycle_count += 2
                else:
                    temp >>= 1
                    cycle_count += 1
            collatz_cycle_list.append(cycle_count)
            if cycle_count >= big_cycle_count:
                big_cycler_under_num = j
                big_cycle_count = cycle_count
            largest_cycler_map[j] = big_cycler_under_num
    print big_cycler_under_num
