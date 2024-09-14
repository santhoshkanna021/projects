import random

user=0
computer=0

options=["rock","paper","scissors"]

print("welcome to the game")


user=input("Do you want to play:")

if user.lower() =="no":
    quit()

else:
    print("let play the game")


while True:

    

    user_type=input("type rock/paper/scissors :").lower()

    

    random_number=random.randint(0,2)


    computer_type=options[random_number]

    print("computer",computer_type)

    if user_type =="rock" and computer_type =="scissors":
        print("you win")
        user +=1

    elif user_type =="paper" and computer_type =="rock":
        print("you win")
        user +=1

    elif user_type =="scissors" and computer_type =="paper":
        print("you win")
        user +=1

    else:
        print("lost")
        computer +=1


    print("you win ",user)

    print("computer win",computer)
   

        

    
    
