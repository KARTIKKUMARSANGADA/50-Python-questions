def second_largest():
    s1 = [4, 3, 1, 2]
    unique_list = list(set(s1))  
    unique_list.sort(reverse=True)
    return unique_list[1]

print(second_largest())

# Output:
