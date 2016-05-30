import bisect
import collections


def get_map_key(target_num, keys):
    key_index = bisect.bisect_left(keys, target_num)
    if key_index < len(keys):
        return keys[key_index]
    else:
        return 0


factor_dict = {1: 3, 3: 6, 5: 28, 8: 36, 15: 120, 17: 300, 19: 528, 23: 630, 35: 2016, 39: 3240, 47: 5460, 89: 25200,
               111: 73920, 127: 157080, 143: 437580, 161: 749700, 167: 1385280, 191: 1493856, 239: 2031120,
               319: 2162160, 479: 17907120, 575: 76576500, 647: 103672800, 767: 236215980, 1023: 842161320}
factor_map = collections.OrderedDict(sorted(factor_dict.iteritems(), key=lambda t: t[0]))
trial_count = int(raw_input())
for i in range(trial_count):
    threshold = int(raw_input())
    print factor_map[get_map_key(threshold, factor_map.keys())]
