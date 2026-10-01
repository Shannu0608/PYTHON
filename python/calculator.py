n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
operation = input("enter any operator")
if operation == "+":
    print(n1 + n2)
elif operation == "-": 
    print(n1 - n2)
elif operation =="*":
    print(n1 * n2)
elif operation == "//":
    print( n1 // n2)
elif operation == "%":
    print(n1 % n2)
else:
    print("invalid operation")
