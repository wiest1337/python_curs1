message = "  пРиВеТ,аГеНт,ЗаДаНиЕ,сЕкРеТнОе,ВсТрЕчА,в,пОлНоЧь  "
code = "Z9a8b7c6d5"

clean = message.strip()
print(len(message))
print(len(clean))
print(clean.lower().count("е"))

words = clean.split(",")
print(words[0])
print(words[-1])
print(message.find("сЕкРеТнОе"))

for i in range(len(words)):
    words[i] = words[i].capitalize()

result = ", ".join(words)
print(result)

print(code[:3])
print(code[-4:])
print(code[::2])
print(code[::-1])

print(words[1:-1])
print(words[::-1])