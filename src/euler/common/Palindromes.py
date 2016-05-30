def num_is_palindromic(num):
    n_as_string = str(num)
    n_len = len(n_as_string)
    middle = n_len / 2
    middle_offset = 0 if n_len % 2 else 1

    return n_as_string[:middle] == n_as_string[:middle-middle_offset:-1]


def is_six_digit_number(n):
    return len(str(n)) == 6


def get_all_six_digit_palindromes():
    left_number = 999
    palindrome_set = set()
    # we just know from inspection that any left number less than 317 is a waste of time
    while left_number > 316:
        right_number = left_number
        while right_number > 99:
            current_product = left_number * right_number
            if not is_six_digit_number(current_product):
                break
            elif num_is_palindromic(current_product):
                palindrome_set.add(current_product)
            right_number -= 1
        left_number -= 1
    return palindrome_set