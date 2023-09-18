"""
mojeCisloTri = 3
mojeCisloCtyri = 4

mojeCisloSedm = mojeCisloTri+mojeCisloCtyri
print(mojeCisloSedm)
print(type(mojeCisloSedm))
#print(mojeCisloSedm == 8 )
#print(type(mojeCisloSedm == 8))
"""

myString1 = "Matouš"
myString2 = " Pikous"

n1 = 1
n2 = 42

# Predani vicero argumentu funkci print()
print("Vypocet:", n1, "+", n2, "=", n1 + n2)
# Rucni pretypovani a spojeni retezce (pred predanim funkci print)
print("Vypocet: " + str(n1) + " + " + str(n2) + " = " + str(n1 + n2))
# Vyuziti F-strings (formated strings)
print(f"Vypocet: {n1} + {n2} = {n1 + n2}")

