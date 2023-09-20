txt = input("Zadej text: ")

slov = 0

isSlovo = False
for i in range(len(txt)):
    if isSlovo == True and txt[i] == " ":
        slov = slov + 1
    elif txt[i] != " ":
        isSlovo = True



print("Slov:", slov + 1)
print("Znaku:", len(txt))