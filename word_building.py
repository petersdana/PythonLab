#Creating the Word Building Game.
#A player enters a word
#The computer or the second player has to enter a word starting with the last letter of the word typed by the first player.
#The words shouldn't be repeated and should be present in the English dictionary (the input dictionary)
#The game continues till a player cannot think of any further words and presses the letter q to quit the game.
# Created By Vandana on 22 Nov, 2019, Friday
import random

print ("\n THE WORD BUILDING GAME")

print ("\n The game will stop when the player enters just letter q")

game_cat = input ("\n Choose whether you want to play against: a) another player or b) against a computer: ")
game_cat = game_cat.lower()


count = 0
findings = 0
player1_word = 'null'
player1_list= []
comp_list = []
dict_list = []
comp_word = 'null'
check = False
#Not initializing special variables for player2. Player2 variables = comp variables

while player1_word != 'Q':
    #print ("\n Here in the beginning")
    findings = 0
    player1_word = input ("\nPlayer1: Enter a word: ")
    player1_word = player1_word.upper()

    if player1_word == 'Q':
        print ("\n Congratulations! You built",len(player1_list),"words\n\n")
        quit()

    if count != 0 and player1_word[0] != last_letter:
        print ("\n Incorrect! Enter word starting with ", last_letter)
        continue
    elif player1_word in player1_list:
        print ("\n Word already used. Enter another word")
        continue
    elif player1_word in comp_list:
        print ("\n Word already used. Enter another word")
        continue

    dictionary = open('dictionary.txt')
    for main_word in dictionary:
        main_word = main_word.strip()
        if main_word == player1_word:
            findings = findings + 1
            #print ("\nfound", findings)

    if findings == 0:
        print ("\n Word doesn't exist in the dictionary. Re-enter the word.")
        continue

    player1_list.append(player1_word)
    count = count + 1

    last_letter = player1_word[len(player1_word)-1]


    #---FOR PLAYER 2 ---------#
    if game_cat == 'a':
        check = False
        print ("\n Last Letter for Player2 is: ", last_letter)
        findings = 0
        while check is False:
            comp_word = input ("\nPlayer2: Enter a word: ")
            comp_word = comp_word.upper()

            if comp_word == 'Q':
                print ("\n Congratulations! You built",len(comp_list),"words\n\n")
                quit()

            if comp_word[0] != last_letter:
                print ("\n Incorrect! Enter word starting with ", last_letter)
                check = False
                continue
            elif comp_word in player1_list:
                print ("\n Word already used. Enter another word")
                check = False
                continue
            elif comp_word in comp_list:
                print ("\n Word already used. Enter another word")
                check = False
                continue

            dictionary = open('dictionary.txt')
            for main_word in dictionary:
                main_word = main_word.strip()
                if main_word == comp_word:
                    findings = findings + 1
                #print ("\nfound", findings)

            if findings == 0:
                print ("\n Word doesn't exist in the dictionary. Re-enter the word.")
                check = False
                continue

            check = True
            
        comp_list.append(comp_word)


        last_letter = comp_word[len(comp_word)-1]
        print ("\n Last Letter for Player1 is: ", last_letter)


    #----FOR COMPUTER WORD ----#

    if game_cat =='b':
        print ("\n Last Letter for Computer is: ", last_letter)

        dictionary = open('dictionary.txt')
        for main_word in dictionary:
            main_word = main_word.strip()
            if main_word[0] == last_letter and main_word not in player1_list and main_word not in comp_list:
            #print ("\n", main_word)
                dict_list.append(main_word) #dict_list = dict_list.append(main_word)

    #print ("\n Word by Computer is: ", dict_list)
        comp_word = random.choice(dict_list)
        comp_list.append(comp_word)
        print ("\n The word by the computer is: ", comp_word)
        last_letter = comp_word[len(comp_word)-1]
        print ("\n Player1 needs to enter a word starting with : ", last_letter)
        dict_list.clear()
    #num = len(player1_list)
    #print(num)

#print ("\n Player list", player1_list)
