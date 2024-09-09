print("welcome to the game")

player=input("do you want to play:")

if player.lower() !="yes":
    quit()

print("ok let play")
score=0

question=input("how many days in a week?")


if question.lower() == "7":
    print("correct")
    score+=1 
    
else:
    print("incorrect")


question=input("How many time zones are there in Russia?")


if question.lower() =="11":
    print("correct")
    score+=1
    
else:
    print("incorrect")


question=input("What’s the national flower of Japan?")


if question.lower() =="Cherry blossom":
    print("correct")
    score+=1
    
else:
    print("incorrect")


question=input("How many stripes are there on the US flag? ")


if question.lower() =="13":
    print("correct")
    score+=1
    
else:
    print("incorrect")


question=input("What’s the national animal of Australia?")


if question.lower() =="Red Kangaroo":
    print("correct")
    score+=1
    
else:
    print("incorrect")

print("your score: "+str(score))
