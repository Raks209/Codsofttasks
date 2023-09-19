# -------ROCK PAPER SCISSOR GAME WITH USE OF PYTHON 
'''
WINNING RULE FOR THIS GAME
FOR ROCK VS PAPER --> PAPER WIN
FOR ROCK VS SCISSOR--> ROCK WIN
FOR PAPER VS SCISSOR--> SCISSOR WIN

'''
import random
list =["Rock","Paper","Scissor"]

#For not terminating the program and keep it continuing in loop , while is used
while True :
    ccount=0
    ucount=0

    userselection = int(input('''
The Game has been start
if you want to play press 1 else 2
                          
1 Yes
2 Exit                         

'''))
    print("Choose one out of these three")
    if userselection==1:
        for x in range(1,4):
            userinp=int(input('''
1 Paper
2 Rock
3 Scissor
                             '''))
            if userinp==1:
                user_ch="Paper"
            elif userinp==2:
                user_ch="Rock"
            elif userinp==3:
                user_ch="Scissor"

            computer_ch=random.choice(list)

            if(user_ch=="Paper" and computer_ch=="Rock") or (user_ch=="Rock" and
             computer_ch=="Scissor") or (user_ch=="Scissor" and computer_ch=="Paper"):
            
                print("Computer Value",computer_ch)
                print("User value",user_ch)
                print("You are the winner of this round")
                ucount=ucount+1
            elif(computer_ch==user_ch):
                 print("Computer Value",computer_ch)
                 print("User value",user_ch)
                 print("This round is draw")
                 ucount=ucount
                 ccount=ccount
            else:
                 print("Computer Value",computer_ch)
                 print("User value",user_ch)
                 print("Computer is the winner of this round")
                 ccount=ccount+1
    if ucount>ccount:
        print("You are the winner of the game")
        print("User points",ucount)
        print("computer point",ccount)
    elif ucount==ccount:
        print("The game has been draw")
        print("User point",ucount)
        print("computer point",ccount)
    else:
        print("Computer is the winner of this  game")
        print("User point",ucount)
        print("computer point",ccount)

else:
    print("Exit")
    
    

