
def divisibleby5(x):
    if x % 5 == 0:
        return True
    else:
        return False

def divisibleby7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def divisibleby9(x):
    if x % 9 == 0:
        return True
    else:
        return False

def divisibleby10(x):
    if x % 10 == 0:
        return True
    else:
        return False

if __name__=="__main__":
    a = int(input("Enter a Number: "))
    result = divisibleby5(a)
    if result == True:
        print(result, "is Divisible by 5")
    else:
        print(result, "is NOT Divisible by 5")

    result2 = divisibleby7(a)
    if result == True:
        print(result, "is Divisible by 7")
    else:
        print(result, "is NOT Divisible by 7")

    result3 = divisibleby9(a)
    if result == True:
        print(result, "is Divisible by 9")
    else:
        print(result, "is NOT Divisible by 9")

    result = divisibleby10(a)
    if result == True:
        print(result, "is Divisible by 10")
    else:
        print(result, "is NOT Divisible by 10")





