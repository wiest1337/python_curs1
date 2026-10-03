hero = {"name": "Артём", "level": 5, "hp": 100}

print(hero["name"])
print(hero.get("level"))

hero["level"] = 6

hero["gold"] = 50
print(hero)

hero.pop("gold")

for key, value in hero.items():
    print(key, "-", value)