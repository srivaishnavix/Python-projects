#Dice roll simulator
import random 
while True:
    print("1.Roll the dice 2.exit")
    user = int(input("Type in your option"))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    else:
        break