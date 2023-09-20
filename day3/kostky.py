import random

nKostek = int(input("Zadej počet kostek: "))
nStran = int(input("Zadej počet stran: "))
nHodu = int(input("Zadej počet hodů: "))

cetnosti = [0] * (nStran * nKostek + 1)

for i in range(nHodu):
    # hod kostkami
    hod = 0
    for j in range(nKostek):
        hod += random.randint(1, nStran)
    # zvys cetnost
    cetnosti[hod] += 1

# vypis cetnosti
# print("Četnosti:")
print(cetnosti)
print("----+---------+---------+------")
print("Hod | Cetnost | Procent | Graf")
print("----+---------+---------+------")
for i in range(nKostek, len(cetnosti)):
    pomer = cetnosti[i] / nHodu * 100
    print(f"{i:4d}| {cetnosti[i]:8d}| {pomer:7.2f}%| {'#' * int(2*pomer)}")
print("----+---------+---------+------")
