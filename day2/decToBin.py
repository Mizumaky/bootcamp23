# decimal to bin

n = int(input("Enter a decimal number: "))

# priklad n=42
# 2 moznosti reseni

# odpredu - kolikrat se vejdou mocniny 2 do n
# najdi nejvetsi mocninu 2, ktera je mensi nez dec
# 2^0 = 1
# 2^1 = 2
# 2^2 = 4
# 2^3 = 8
# 2^4 = 16
# 2^5 = 32 <----
# 2^6 = 64 STOP
# 
# pote jdi od nejvetsi mocniny, vzdy
# 42 // 32 = 1 (kolikrat se vejde 2^5=32 do 42)
# 42 % 32 = 10 (kolik nam zbyde)
# 10 // 16 = 0 (kolikrat se vejde 2^4=16 do 10)
# 10 % 16 = 10 
# 10 // 8 = 1 (kolikrat se vejde 2^3=8 do 10)
# 10 % 8 = 2 
# 2 // 4 = 0 (kolikrat se vejde 2^2=4 do 2)
# 2 % 4 = 2 
# 2 // 2 = 1 (kolikrat se vejde 2^1=2 do 2)
# 2 % 2 = 0
# 0 // 1 = 0 (kolikrat se vejde 2^0=1 do 0)
# 0 % 1 = 0

mocnina = 1
while mocnina <= n:
    mocnina = mocnina * 2
mocnina = mocnina // 2  # vratim se o jednu mocninu zpet

while mocnina > 0:
    print(n // mocnina, end="")  # kolikrat se vejde aktualni mocnina do n
    n = n % mocnina  # kolik nam zbyde
    mocnina = mocnina // 2  # posunu se na dalsi mocninu

# odzadu - vyuzivame zbytek po deleni vyssi mocninou 2
# 2^0 -> 42 % 2 = 0  (zbytek po deleni nka 2^1=2) - delime poprve 2 (zjistujeme posledni bit - liche/sude)
#        42 // 2 = 21
# 2^1 -> 21 % 2 = 1  (zbytek po deleni nka 2^2=4) - delime podruhe 2 (predposledni bit)
#        21 // 2 = 10
# 2^2 -> 10 % 2 = 0  (zbytek po deleni nka 2^3=8)
#        10 // 2 = 5
# 2^3 -> 5 % 2 = 1   (zbytek po deleni nka 2^4=16)
#        5 // 2 = 2
# 2^4 -> 2 % 2 = 0   (zbytek po deleni nka 2^5=32)
#        2 // 2 = 1

txt = ""
while n > 0:
    zbytek = n % 2 
    txt = str(zbytek) + txt  # pridam novou cislici pred to co uz mam
    n = n // 2  # postupne delim 2 a zmensuji n
print(txt)