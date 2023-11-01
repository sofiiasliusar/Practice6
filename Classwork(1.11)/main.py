# Робота з файлами, створення функції
import math

file = open('input.txt', 'r') # r - читати, w - перезаписує повністю, a - додає
#  a = list(map(float, file.read().split(" "))) розписано:
a = file.read()
a = a.split(" ") #\n і кожен елемент у файлі з нового рядка
b = list(map(float,a))
print(a)
print(b)
c = list()
for i in range(len(a)):
    temp = float(a[i])
    c.append(temp)
print(c)

c[1] = c[2] + c[3]
c[2] = c[1] - c[2]
out_text = list(map(str, c))
f = open('output.txt', 'w')
for out_text in c:
    f.write(str(out_text) + ' ')
file.close()