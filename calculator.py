a = float(input("Enter the first number: "))
op = input("Enter an operator (+, -, *, /): ")
b = float(input("Enter the second number: "))
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b) 
elif op == "*":
    print(a * b)
elif op == "/": 
    if b == 0:
        print("Error: Division by zero is not allowed.")    
    else:
        print(a / b)    
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")