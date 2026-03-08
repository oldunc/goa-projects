def sash(num1,num2,num3,num4,num5):
    a = num1 + num2 + num3 + num4 + num5
    b = a/5
    return b
print(sash(5,5,5,5,5))

def sayhi(name = "human"):
    print("hello" " " f"{name}")

sayhi()


def capitalize(name):
    return name.upper()

print(capitalize("hello"))