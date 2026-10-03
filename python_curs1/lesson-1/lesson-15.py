def greet(name):
    print("Привет,", name + "!")

greet("Руслан")
greet("Анна")

def add(a, b):
    return a + b

result = add(5, 7)
print(result)

def find_max(lst):
    max_number = lst[0]
    for item in lst:
        if item > max_number:
            max_number = item
    return max_number

print(find_max([3, 9, 2, 7]))

square = lambda x: x * x
print(square(6))