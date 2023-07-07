n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
operator = input("Select operation: +, -, *, /,%,//,** \n")

if operator == "+":
    print(n1, "+", n2, "=", n1+n2)

elif operator == "-":
    print(n1, "-", n2, "=", n1-n2)

elif operator == "*":
    print(n1, "*", n2, "=", n1*n2)

elif  operator== "/":
    print(n1, "/", n2, "=", n1/n2)

elif operator == "%":
    print(n1, "%", n2, "=", n1%n2)

elif operator == "//":
    print(n1, "//", n2, "=", n1//n2)

elif operator == "**":
    print(n1, "**", n2, "=", n1**n2)
    
else:
    print("Invalid input")