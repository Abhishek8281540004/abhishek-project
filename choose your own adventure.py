name=input("type your name: ")
print("welcome", name, "to this adventure.")

answer=input("you are on a dirty road, it has come to an end and you can go left or right, which way do you like to go left or right? ").lower()

if answer=="left":
    answer=input("you come to a road, you can walk or swim: ")

    if answer=="swim":
        print("you swim across and got eaten by alligator")

    elif answer =="walk":
        print("you walk many km run out of water and died")

    else:
        print("not valid option. you lose.")
        
elif answer=="right":
    answer=input("you ,come to a bridge do you wanna cross it or go back ")
    if answer=="back":
        print("you go back you lose ")

    elif answer =="cross":
        answer=input("you cross the bridge, you saw a stranger do you want to talk to him, yes/no? ")
        if answer=="yes":
            print("you talk to the stranger and they give you gold! you win")

        elif answer=="no":
            print("you ignored the stranger and they kill you")

        else:
            print("not valid option. you lose.")

    else:
        print("not valid option. you lose.")
    print()

else:
    print("not valid option. you lose.")

print("thank you for trying", name)