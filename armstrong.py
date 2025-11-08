num = int(input("Enter your number:"))

num_str = str(num)
num_digits = len(num_str)

sum_of_powers=0
temp_num = num 


while temp_num > 0:
    digit = temp_num % 10          # Extract the last digit
    sum_of_powers += digit ** num_digits  # Add digit^num_digits to sum
    temp_num //= 10                # Remove the last digit

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
