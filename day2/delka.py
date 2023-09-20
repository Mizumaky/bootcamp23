txt = input("Zadej text: ")

slov = 0

for i in range(len(txt)):
    if txt[i] == " ":
        slov = slov + 1


print("Slov:", slov + 1)
print("Znaku:", len(txt))