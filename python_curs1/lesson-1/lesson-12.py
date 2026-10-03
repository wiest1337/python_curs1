inventory = ("меч", "щит", "зелье", "зелье", "ключ", "зелье", "карта")

print(len(inventory))
print(inventory.count("зелье"))
print(inventory[0])
print(inventory[-1])
print(inventory[1:4])

for item in inventory:
    print(item)

temp = list(inventory)
temp.append("золото")
inventory = tuple(temp)
print(inventory)

reward = ("награда",)
print(type(reward))

print(tuple("меч"))

inventory[0] = "лук"