import math

file = open('input.txt', 'r')
x = file.read()
x = float(x)
print("x = ", x)

c = math.sin(math.cos(x) - 1)*(math.e**2)
y = 1 + math.log(3 + abs(x))

print(c)
print(y)

out_text = c, y
f = open('output.txt', 'w')
f.write(out_text)
