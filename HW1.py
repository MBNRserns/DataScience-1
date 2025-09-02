import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("What numbers are in the first matrix? use spaces between numbers:")
m1 = np.array(list(map(float, input().split()))).reshape(rows, cols)

print("What numbers are in the second matrix? use spaces between numbers:")
m2 = np.array(list(map(float, input().split()))).reshape(rows, cols)

print("Choose operation: + for addition, - for subtraction")
operation = input("Enter operation (+ or -): ")

if operation == '+':
    result = m1 + m2
elif operation == '-':
    result = m1 - m2
else:
    print("That operation isn't valid")
    exit()

print("Result:")
print(result)
