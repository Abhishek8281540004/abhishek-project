print("welcome to my computer quiz game")
playing=input(" do you want to play? ")
if playing.lower() !="yes":
    quit()

print("okay! lets's play")
score = 0

answer=input("what is cpu? ")
if answer.lower()=="central processing unit":
    print("thats correct")
    score += 2
else:
     print("incorrect")
     score -=1

answer=input("what is gpu? ")
if answer.lower()=="graphic processing unit":
    print("thats correct")
    score += 2
else:
     print("incorrect")
     score -=1

answer=input("what is RAM? ")
if answer.lower()=="random access memory":
    print("thats correct")
    score += 2
else:
     print("incorrect")
     score -=1   

answer=input("what is ROM? ")
if answer.lower()=="read only memory":
    print("thats correct")
    score += 2
else:
     print("incorrect")
     score -=1


print("your score is " + str(score))
print("you got "+ str((score/4) * 100) +"%. ")   

