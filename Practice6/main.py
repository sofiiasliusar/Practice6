import math

with open("input.txt", "r") as in_text:
    x =float(in_text.read())
def calculatec(x):
    c = math.sin(math.cos(x)-1)*(math.e**2)
    return c

def calculatey(x):
    y = 1 + math.log(3 + abs(x))
    return y

c = calculatec(x)
y = calculatey(x)

print("x = ", x)
print("c = ", c)
print("y = ", y)

with open("output.txt", "w") as out_text:
    out_text.write(f"{x}\n")
    out_text.write(f"{c}\n")
    out_text.write(f"{y}\n")


