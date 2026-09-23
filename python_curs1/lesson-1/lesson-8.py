age = int(input("Введите ваш возраст: "))
has_ticket = True

if age < 18:
    print("Вход запрещён, вы несовершеннолетний")
elif age >= 18 and has_ticket:
    print("Добро пожаловать в клуб!")
else:
    print("Нужен билет, чтобы войти")

status = "взрослый" if age >= 18 else "ребёнок"
print(status)