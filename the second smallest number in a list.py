def second_smallest(lst):
    unique_list = sorted(set(lst))
    return unique_list[1]
lst=[4, 3, 1, 2]
print(second_smallest(lst))  # Output: 2
