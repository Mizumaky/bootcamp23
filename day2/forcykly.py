



for kocicka in range(5,10,2):
    print(kocicka)    
print("Konec cyklu")

pejsek = 3.14
for kocicka in range(10,int(pejsek),-1):
    print(kocicka)    

print("Konec cyklu")

for kocicka in "bootcamp je super":
    print(kocicka) 

print("Konec cyklu")

for i in [2,3,5,"zelvicka",11,13,17,19,23,29]: 
    print(i)

print("Konec cyklu")

jePrvocislo = True
for i in range(10):
    print("   i: ",i)
    if 13 % i ==0:
        jePrvocislo = False
        break



"""
for i in range(5,10,2):
    print(i)

for i in "bootcamp je super":
    print(i)

for i in range(10,5,-2):
    print(i)

for i in range(10,5,-2):
    print(i)

print(f"Icko: {i}")
"""