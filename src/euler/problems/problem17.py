#yet another lame problem

numerals = [" One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"]
tens_place = [" Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
teens = [" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
hundred = " Hundred"
magnitudes = ["", " Thousand", " Million", " Billion", " Trillion"]
mag_count = len(magnitudes) - 1


def long_name(n):
    nlist = list(str(n))
    n_nums = map(int, ['0'] * (13 - len(nlist)) + nlist)
    index = 0
    is_teen = False
    have_digits = False
    name = ""
    while index < 13:
        numeral_value = n_nums[index]
        if numeral_value is 0 and not is_teen:
            if have_digits and not index % 3:
                name += magnitudes[mag_count - (index / 3)]
                have_digits = False
            index += 1
            continue
        elif not (index + 1) % 3:
            if numeral_value is 1:
                is_teen = True
            else:
                name += tens_place[numeral_value - 2]
            have_digits = True
        else:
            if is_teen:
                name += teens[numeral_value]
                is_teen = False
            else:
                name += numerals[numeral_value - 1]
            have_digits = True

        if not index % 3:
            name += magnitudes[mag_count - (index / 3)]
            have_digits = False
        elif not (index + 2) % 3:
            name += hundred

        index += 1
    if len(name) == 0:
        name += " Zero"
    return name[1:]


trial_count = int(raw_input())
for i in range(trial_count):
    n = int(raw_input())
    print long_name(n)
