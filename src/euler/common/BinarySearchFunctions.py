import bisect


def get_value_below(num, items):
    """
    Finds the first value found in items which is less than the given number
    :param num: The target number
    :param items: The list/data structure to search
    :return: The first value below num, should it exist
    """
    index = bisect.bisect_right(items, num)
    if 0 <= index < len(items):
        return items[index]
    else:
        raise ValueError("Value below number does not exist.")


def get_value_above(num, items):
    """
    Finds the first value found in items which is greater than the given number
    :param num: The target number
    :param items: The list/data structure to search
    :return: The first value above num, should it exist
    """
    index = bisect.bisect_left(items, num)
    if 0 <= index < len(items):
        return items[index]
    else:
        raise ValueError("Value above number does not exist")
