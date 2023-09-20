n1 = 1
n2 = 42
n3 = 42.124245
digits = 4

print(f"n1 = {n1}")
print(f"n2 = {n2:08d}")
print(f"n3 = {n3:8.2f}")
print(f"n3 = {n3:8.{digits}f}")

print("n1 = {}".format(n1))
print("n2 = {:08d}".format(n2))
print("n3 = {:8.2f}".format(n3))
print("n3 = {:8.{}f}".format(n3, digits))

print("n1 = %d" % n1)
print("n2 = %08d" % n2)
print("n3 = %8.2f" % n3)
print("n3 = %8.*f" % (digits, n3))


