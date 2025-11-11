numbers = []

n = int(input("How many numbers do you want to enter: "))

for i in range (n):
    num = int(input(f"Enter number{i+1}: "))
    numbers.append(num)

if len(numbers) < 2:
    print("Not enough numbers to determine the second largest.")
else:
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    
second_largest = unique_numbers[1]
print("The second largest number is:", second_largest)
