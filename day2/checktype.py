x = input("Enter something: ")

if x.isnumeric():
    print("You entered an integer")
elif x.isalpha():
    print("You entered only letters")
elif x.isalnum():
    print("You entered letters and numbers")
else:
    try:
        float(x)
        print("You entered a floating point number")
    except ValueError:
        print("You entered something else")