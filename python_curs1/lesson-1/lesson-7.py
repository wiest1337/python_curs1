
name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
height = float(input("Введите ваш рост (например 1.75): "))

is_adult = True

print("Имя: " + name + ", Возраст: " + str(age) + ", Рост: " + str(height))

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Сумма: " + str(num1 + num2))
print("Разность: " + str(num1 - num2))
print("Произведение: " + str(num1 * num2))
print("Деление: " + str(num1 / num2))
print("Целочисленное деление: " + str(num1 // num2))
print("Остаток от деления: " + str(num1 % num2))
print("Возведение в степень: " + str(num1 ** num2))

title = "Привет "
print(title * age)

del is_adult
is_adult = 1
print(is_adult)
