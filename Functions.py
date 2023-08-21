""""
there are 4 types of functions
1. function without parameters and function without return types
2. function with perametersa and function with return types
3. function with perameters and function without return type
4. function without perameter and function with return type
"""

def sum(): # without perameter and without return type
    x = int(input("enter the number:"))
    y= int(input("enter number:"))
    ans= x +y

    print(ans)
sum()

def mul(num1,num2):# with perameter and function without return types
    
    ans= num1 * num2
    print(ans)
num1 = int(input("enter the number:"))
num2= int(input("enter number:"))

mul(num1,num2)

def sub(num1,num2): # with perameter and function with return type
    sub= num1-num2
    return sub
num1 = int(input("enter the number:"))
num2= int(input("enter number:"))
print(sub(num1,num2))

def div():#without perameter and funvction with return type
    num1 = int(input("enter the number:"))
    num2= int(input("enter number:"))
    ans = num1/num2
    return ans
print(div())

