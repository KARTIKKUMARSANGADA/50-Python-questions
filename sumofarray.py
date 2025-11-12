arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(0, n):
    ele = int(input(f"Enter element:{i+1}: "))
    arr.append(ele) 
    
ans = sum(arr)
print('Sum:', ans)