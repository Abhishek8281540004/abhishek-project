import random 

print("welcome to hangman game")

options=["cat", "dog", "cow", "horse", "zebra"]

word=options[random.randint(0, 4)]




chance=4
while True:
    
    user_guess=input("guess the letters: ")
    if chance==0:
        print("your chance is over")
        break

    if user_guess in word:
        print("thats correct")
        chance-=1
        continue
 
    elif user_guess not in word:
        print("incorrect")
        chance-=1
        continue
        
 
        

print("you got only 5 chances")    


   


        





































