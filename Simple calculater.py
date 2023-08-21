# simple calculator program
# contains +,-,*,/


num1 = int(input("Enter the number:"))
num2 = int(input("enter the number:"))
ope = input("enter operator")

if ope == "+":
    print(num1+num2)
elif ope == "-":
    print(num1 - num2)
elif ope == "/":
    print(num1/num2)
elif ope == "*":
    print(num1*num2)
else:
    print("invalid operators")
