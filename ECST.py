import random


print("Hello. Welcome to ECST, the evolved, superior version of PCPA. If you are here, then it must indicate that you have overcome PCPA. Well done.")
q = input("Do you want to play an eternal cycle of suffering and torment? ").capitalize() 
while True:
    
    if q == "Yes": 

        rannum = random.randint(1,1000000000000) 

        answer = int(input("What is the outputted number? "))


        if answer == rannum: 

            print("You got it correct, well done") 

        else: 

            print("Try again") 

    else:
        print("Too bad, I don't care")
        
        while q != "Yes":
            

            rannum = random.randint(1,1000000000000) 

            answer = int(input("What is the outputted number? "))

            if answer == rannum: 

                print("You got it correct, well done. Now redo it")
            else:
                print("You're an idiot")
