def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """
    a=data.index(max(data))

    return a
print(find_max_index([1, 2, 3, 4, 5]))
print(find_max_index([6, 8, 7, 4, 0]))
