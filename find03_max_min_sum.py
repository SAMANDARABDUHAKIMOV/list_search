def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    a=max(data)
    b=min(data)
    c=a+b
   

    return c
data= [1, 2, 3, 4, 5]
print(find_max_min_sum( [1, 2, 3, 4, 5]))
print(find_max_min_sum([2, 7, 3, 4, 9]))

