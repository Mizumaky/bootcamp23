# check for prime numbers
a = int(input("Enter a number: "))
if a <= 1:
    print("Enter a number greater than 1")
else:
    # zkousej delit cislo a cisly od 2 do a-1
    for i in range(2, a):
        # pokud je zbytek po deleni 0, tak to neni prvocislo
        if (a % i) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
        # pokud vyzkousime vsechna cisla a zadne nevydeli a, tak je to prvocislo
    
