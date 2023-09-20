"""
myArr1 = [1,2,3]

# myArr2 = myArr1  
myArr2 = myArr1.copy()
# myArr2 = []
# myArr2.extend(myArr1)
myArr1[2] = "ahoj"

print(myArr1)
print(myArr2)

"""
add = 50
cislo = 50
"""
while add >= 1:
    binar_y_n = int(input("je vetsi nez" + str(cislo)+ "?") )
    if binar_y_n == 1:
        cislo = cislo + add
    elif binar_y_n == 0:
        cislo = cislo - add
    add = add // 2
print(cislo)
"""

while add >= 1:
    binar_y_n = input("je vetsi nez" + str(cislo)+ "? ") == "y"
    b = binar_y_n
    cislo += b*add + (1-b)*(-add)
    add = add // 2
print(cislo)
