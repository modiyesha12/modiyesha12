# normal function
def my(num):
    if num % 2 == 0:
        print("number is even")
    else:
        print("number is odd")


num = int(input("enter your number"))
print(my(num))

print("======> lambada function")


def ans(num): return num * num


print(ans(12))
