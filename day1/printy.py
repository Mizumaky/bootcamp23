n1 = 1
n2 = 42

x = 42.124245
print(f"x={x:4.2f}")

# Predani vicero argumentu funkci print()
print("Vypocet:", n1, "+", n2, "=", n1 + n2)
# Rucni pretypovani a spojeni retezce (pred predanim funkci print)
print("Vypocet: " + str(n1) + " + " + str(n2) + " = " + str(n1 + n2))
# Vyuziti F-strings (formated strings)
print(f"Vypocet: {n1} + {n2} = {n1 + n2}")
# old style formatovani
print("Vypocet: %d + %d = %d" % (n1, n2, n1 + n2))
# formatovani pomoci metody format()
print("Vypocet: {:2f} + {} = {}".format(n1, n2, n1 + n2))

