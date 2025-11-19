file_name = "sample.txt"   # change file name accroding to your file

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        print("Total number of lines:", len(lines))

except FileNotFoundError:
    print("Error: File not found!")
