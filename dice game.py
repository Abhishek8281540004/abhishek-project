import random

print("welcome to dice rolling game!")

user_input=input("do you want to play type yes to play or q to quit:  ").lower()

if user_input=="yes":
    print("lets start the game")

elif user_input=="q":
    quit()

else:
    print("please type coorect input next time")
    quit()

points=0

while True:
    
    dice=random.randint(0,6)

    user=input("type r to roll or q to quit: ")

    if user=="r":
        print("you got", dice)
        points+=dice
        continue

    elif user=="q":
        break

    else:
        print("please type correct input")
        
 #use break statement to break the while loop then only codes outside the while loop will work    
print("you got", str(points), "points.")

print("thank you for playing :)")
