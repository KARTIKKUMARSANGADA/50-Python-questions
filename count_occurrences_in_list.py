n = int(input("How many elements do you want to enter:"))
numbers = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

dict_count = {}

for item in numbers:
    if item in dict_count:
        dict_count[item] += 1
    else:
        dict_count[item] = 1

print("Element occurrences:")
for key, value in dict_count.items():
    print(f"{key}: {value} time(s)")
    