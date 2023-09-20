n = int(input("Enter a number: "))
#for j in range(2, n):
j = 1
podminka = n % 2 == 0
while True:
while podminka:
    j = j + 1
    # check for prime numbers
    a = j
    if a <= 1:
        print("Enter a number greater than 1")
    else:
        # pomocna / flag promenna
        foundDivisor = False
        # zkousej delit cislo a cisly od 2 do a-1
        for i in range(2, a):
            # pokud je zbytek po deleni 0, tak to neni prvocislo
            if (a % i) == 0:
                foundDivisor = True
                # print(a, "is not a prime number")
                break
        # pokud vyzkousime vsechna cisla a zadne nevydeli a, tak je to prvocislo
        # if foundDivisor == False:
        if not foundDivisor:   
            # print(a, "is a prime number")
            print(a)