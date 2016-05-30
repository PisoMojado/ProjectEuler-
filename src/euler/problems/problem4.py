from euler.common.Palindromes import get_all_six_digit_palindromes

sorted_palindromes = list(get_all_six_digit_palindromes())
sorted_palindromes.sort(reverse=True)
# we now have all the palindromes in a reverse sorted list
# we'll tackle the problem at this point in the code:
trials = int(raw_input())
for i in range(trials):
    current_N = int(raw_input())
    for j in sorted_palindromes:
        if j < current_N:
            print(j)
            break
