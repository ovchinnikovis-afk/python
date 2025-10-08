import math
num = int(input("Введите целое число: "))
if num >= 0:
    result = math.sqrt(num)
    print("корень числа=",(result))
else:
    result = num * num 
    print("квадрат числа=",(result))