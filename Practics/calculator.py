print("Simple Calculator")
print("Choose an operation: +, -, *, /")

op = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)
else:
    print("Invalid operation!")
