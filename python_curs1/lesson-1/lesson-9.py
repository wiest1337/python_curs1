n = int(input("С какого числа начать отсчёт: "))

while True:
    print(n)
    if n == 0:
        print("Пуск!")
        break
    n -= 1

code = input("Введите кодовое слово: ")

for letter in code:
    if letter == " ":
        continue
    if letter == "х":
        print("Обнаружен сбой!")
        break
else:
    print("Код принят, полёт разрешён")