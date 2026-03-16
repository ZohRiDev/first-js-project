import time

print("Текущее время:", time.ctime())

print("---ДОБРО ПОЖАЛОВАТЬ НА ТЕСТ CВОЕГО ФАВОРИТА В ВИДЕОКАРТАХ---")
print("У тебя 4 секунды на раздумья!")
#time.sleep(4) # Пауза для драматизма

#ans = input("AMD или NVIDIA?")

#if ans.upper() == "AMD":
    #print("Красавчик, любить много fps это твоё, выгодный вариант, но без трассировки лучей")
#if ans.upper() == "NVIDIA":
    #print("Красивая картинка с лучами твой фаворит, но будь готов переплачивать за бренд зелёных)")
 
name = ("айти говно,ура месим") # str показывает текст
age = 16 # int показывает целое число
svg = 4.25 # float показывает не только целые числа 
I143 = True  
print(type(name)) # type показывает класс переменной(данных) name
print(type(age)) # type показывает класс переменной(данных) age
print(type(svg)) # type показывает класс переменной(данных) float
print(type(I143)) # type показывает класс переменной(данных) bool

# input("комментарий")
#name2 = input("Введите своё имя: ") # input всегда выдаёт тип данных str 
#3print("Ваше имя: ",name2)

#name3 = int(input("Введите любое число: ")) # но это можно изменить, поставив перед input тип данных который вам нужен, в моём случае это число
#print("Ваше значение: ",name3)
#print("Тип данных: ",type(name3))

name4 = ("и мне так хорошо с тобо-о-ой")
name5 = ("Держи меня не отпускай,")
print("Я поднимаюсь над землёй,", name4)
print(name5,"между нами ра-a-aй!")
print("Я поднимаюсь над землёй,", name4)
print(name5,"между нами ра-a-ай!")

print("гений")

result = 5 + 10 # сложение
result2 = 10 - 9 # вычитание
result3 = 10 * 5 # умножение
result4 = 7 / 4 # деление вернёт float
print(result4, type(result4))
result5 = 7 // 4 # деление вернёт int
print(result5, type(result5))
result6 = 7 % 4 # деление вернёт int
print(result6, type(result6))

result7 = 4**3
print(result7, type(result7))

num1 = -134
abs_num = abs(num1) # abs это модуль, убирает минус
print(abs_num)

num1 = "hello" # прелесть пайтона, ему плевать на какой у тебя тип данных
print(num1)

num2 = 35
num2 = str(num2)
num3 = float(num2)
print(num2,type(num2)) 
print(num3,type(num3)) 

num4 = int(input('Введите число: '))
#num5 = int(input('Введите число второе: '))
#print("Ответ:", num4 + num5)

# bool - True(1) and False(0)

# Есть знаки которые определяют True и False при сравнении чисел:  
# >=  
# <=
# >
# <
# Равно обозначается ==
# Но есть знак НЕ равно !=
# and - И (*)   or - ИЛИ (+)
#usl1 = num4 > 10 and num4 % 2 == 0 # True and True -> 1 * 1 = 1 = True
#usl2 = num4 < 10 and num4 % 2 == 0 # True and False -> 1 * 0 = 0 = False
#print(usl1)
#print(usl2)

# Введу 60
#usl3 = num4 % 3 == 0 or num4 > 100 # True and False -> 1 + 0 = 1 = True

if num4 > 10 and num4 % 2 == 0:
    print('Условие больше 10 и чётное')
elif num4 % 2 != 0:
    print('Число нечётное')
elif num4 == 7:
    print('Вы ввели 6')
else:
    print('Poka') 

print('КОНЕЦ') 

uk1 = True
print(not(uk1)) # not меняет знак, обозначет НЕ