import time
print("")
print("<< Sud-o-meter >>")
time.sleep(1)
d = int(input("Please, enter the desired diameter of the sud: "))
v = int(input("Please, enter the desired height of the sud: "))
w = int(input("And now, please tell me, how many liters of water do you wanna stuff inside? "))
print("Okay... give me a sec...")
time.sleep(1)
r=d/2
V=(3.14*r**2*v)*1000
if(V>w):
    print("Sooo... your sud is gonna be able to hold",V,"liters of water, and you desired",w,"? That should go fine! GJ Bruh, you did da maths well!")
else:
    print("Sooo... your sud is gonna be able to hold",V,"liters of water, and you desired",w,"?!? You kiddin me?! How the f**k do you wanna get",w,"liters of beer-ehm-water inside this lil sud? I am very disappointed by you...")