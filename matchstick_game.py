#Created on 7th Nov 2019, Thursday by learning from Python For Everyone
#lecture on FutureLearn.


#Basic Introduction to the Game and Rules
#This is a game where two players can play. For single player game refer to Game.py

print ("\n\t\tWELCOME TO THE MATCHSTICK GAME!")
print ("\n Instructions on how to play the game:")
print ("\n 1. The player chooses one or two matchsticks from a set of 10 matchsticks")
print ("\n 2. The second player (or computer) then chooses one or two matchsticks from the remaining matchsticks")
print ("\n 3. The player who gets the last matchstick is declared the winner")
print ("\n\tSo get ready!!\n")

player1_name = input('Please enter first player\'s name: ')
print ("\n If you want to play against the computer please press enter instead of the second player\'s name")
player2_name = input('\nPlease enter second player\'s name: ')

if player2_name == "":
    player2_name = "computer"

print ("\n\t Lets play",player1_name, "Vs", player2_name)

n=10 #Total number of matchsticks
while n >= 1:
     player1_stick = input ("\nPlayer_1: Choose either 1 or 2 matchsticks from the set of matchsticks: ")
     temp_n = n - int(player1_stick)
     if int(player1_stick) <= 0 or int(player1_stick) > 2 or temp_n < 0 :
         player1_stick = input ("\n Wrong value entered. Please enter again: ")

     n = n - int(player1_stick)

     if int (n) == 0 :
         print ("\n\t\tCONGRATULATIONS!", player1_name,"WON THE GAME!!")
         break
     else:
         if player2_name == "computer":
             if  int(n) == 2 or int(n) == 1:
                 print ("\n\tThe Computer Won the Game! Better luck next time!")
                 break
             #Giving random values to the choice of sticks the computer chooses
             if int(n) == 7 or int(n) == 8 or int(n) == 6 or int (n) == 5:
                 computer_stick = 2
             else:
                 computer_stick = 1
         else:
             computer_stick = input ("\nPlayer_2: Choose either 1 or 2 matchsticks from the set of matchsticks: ")
             temp_n = n - int(computer_stick)
             if int(computer_stick) <= 0 or int(computer_stick) > 2 or temp_n < 0 :
                 computer_stick = input ("\n Wrong value entered. Please enter again: ")

     n = n - int(computer_stick)

     if player2_name != "computer":
         if  int(n) <= 0:
             print ("\n\t\tCONGRATULATIONS!",player2_name, "WON THE GAME!!")
             break
         else:
             print ("\nThe remaining matchsticks are",n)
     else:
         print ("\nThe number of sticks that the computer has chosen is:", computer_stick)
         print ("\nThe remaining matchsticks are",n)

print ("\n\n\t\tGAME ENDS\n\n")
