import time

print("Текущее время:", time.ctime())

print("--- ДОБРО ПОЖАЛОВАТЬ В ТРЕНАЖЕР ZOHRIDEV ---")
print("Твой Acer Aspire 3 готов. У тебя 5 секунд на раздумья!")
time.sleep(2) # Пауза для драматизма

ans = input("AMD или NVIDIA?")

if ans.upper() == "AMD":
    print("Красавчик, любить много fps это твоё, выгодный вариант, но без трассировки лучей")
if ans.upper() == "NVIDIA":
    print("Красивая картинка с лучами твой фаворит, но будь готов переплатить)")
