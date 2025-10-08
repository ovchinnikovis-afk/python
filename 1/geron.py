from math import sqrt
print('Эта программа вычисляет площадь треугольника по формуле Герона')
print('Введите длины сторон треугольника\n')
a=float(input('\n'))
b=float(input('\n'))
c=float(input('\n'))
p=(a+b+c)/2
s=sqrt(p*(p-a)*(p-b)*(p-c)) 
print('Площадь треугольника равна %.2f ' %s)
input('Нажмите ENTER')
