'''
a="буря небо кроет \n Вихри снежные крутя"
print(a)
b="message:\n\"hello world\""
print(b)
c=r"C:\python\name.txt"
print(c)
 name=input("как вас зовут?")
print(f"привет,{name}")
a=int(input("Введите число:"))
b=a+5
print(b)
print(5+6)
print(9-5)
print(2*7)
print(6/3)
print(7//3)#Целочисленное деление
print(7%3)#остаток от деления
print(2**5)#возведение в степень
#ариифметические операции с присвоением
a=5
a+=5#присвоение через сложение
a-=6
a*=2
a/=2
a**=2
print(a)
#округление
a=2.0001
b=5
print(round(a/b,5))
print(round(2.0001+0.1))
print(round(2.49))
print(round(2.51))
print(round(2.5))
print(round(3.5))
#Математическиие функции
import math
print(math.sqrt(144))
print(math.ceil(2.5))
print(math.floor(3.5))
print(math.factorial(5))
print(math.sin(0))
print(math.cos(1))
print(math.tan(1))
print(math.log(4, 2))
print(math.log(1))#натуральный логарифм
print(math.log10(5))
print(math.pi)
print(math.fabs(-1))
#решение уравнения
x=float(input())
x1=math.sin(x)+math.cos(x)**2
print(x1)
x2=x**2+math.exp(-x)
print(x2)
x3=2*math.log(x2)
print(x3)
x4=math.sqrt(x1/x3)
print(x4)
x5=1/(1+1/(2*x)+math.fabs(x))
print(x5)
Q=x4+x5
print(round(Q, 2))
'''
a=5
print(f"{a:0b}")#Вывод в двоичной системе
print(f"{a:0o}")#Вывод в восьмиричной системе
print(f"{a:0x}")#Вывод в шестнадцетиричной системе

a=2
b=5
c=a&b#Логическое умножение
print(f"{c},{c:0b}")

d=a|c#логическое сложение
print(f"{d},{d:0b}")
